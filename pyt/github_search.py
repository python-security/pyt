import os
import re
import requests
import sys
import time
from abc import (
    ABCMeta,
    abstractmethod
)
from datetime import (
    date,
    datetime,
    timedelta
)
from . import repo_runner
from .analysis.constraint_table import initialize_constraint_table
from .analysis.fixed_point import analyse
from .argument_helpers import VulnerabilityFiles
from .ast_helper import generate_ast
from .expr_visitor import make_cfg
from .formatters import (
    json,
    text
)
from .project_handler import (
    get_directory_modules,
    get_modules
)
from .repo_runner import (
    add_repo_to_csv,
    get_repos,
    NoEntryPathError
)
from .vulnerabilities import find_vulnerabilities


DEFAULT_TIMEOUT_IN_SECONDS = 60
GITHUB_API_URL = 'https://api.github.com'
GITHUB_OAUTH_TOKEN = None
NUMBER_OF_REQUESTS_ALLOWED_PER_MINUTE = 30  # Rate limit is 10 and 30 with auth
SEARCH_CODE_URL = GITHUB_API_URL + '/search/code'
SEARCH_REPO_URL = GITHUB_API_URL + '/search/repositories'


def set_github_api_token():
    global GITHUB_OAUTH_TOKEN
    try:
        GITHUB_OAUTH_TOKEN = open(
            'github_access_token.pyt',
            'r'
        ).read().strip()
    except FileNotFoundError:
        print('Insert your GitHub access token'
              ' in the github_access_token.pyt file in the pyt package'
              ' if you want to use GitHub search.')
        exit(0)


class Query:
    def __init__(
        self,
        base_url,
        search_string,
        repo=None,
        time_interval=None,
        per_page=100
    ):
        repo = self._repo_parameter(repo)
        time_interval = self._time_interval_parameter(time_interval)
        search_string = self._search_parameter(search_string)
        per_page = self._per_page_parameter(per_page)
        parameters = self._construct_parameters([
            search_string,
            'language:python',
            repo,
            time_interval,
            per_page
        ])
        self.query_string = self._construct_query(base_url, parameters)

    def _construct_query(self, base_url, parameters):
        query = base_url
        query += '+'.join(parameters)
        return query

    def _construct_parameters(self, parameters):
        r = list()
        for p in parameters:
            if p:
                r.append(p)
        return r

    def _search_parameter(self, search_string):
        return '?q="' + search_string + '"'

    def _repo_parameter(self, repo):
        if repo:
            return 'repo:' + repo.name
        else:
            return None

    def _time_interval_parameter(self, created):
        if created:
            p = re.compile('\d\d\d\d-\d\d-\d\d \.\. \d\d\d\d-\d\d-\d\d')
            m = p.match(created)
            if m.group():
                return 'created:"' + m.group() + '"'
            else:
                print('The time interval parameter should be '
                      'of the form: "YYYY-MM-DD .. YYYY-MM-DD"')
                exit(1)
        return None

    def _per_page_parameter(self, per_page):
        if per_page > 100:
            print('The GitHub api does not allow pages with over 100 results.')
            exit(1)
        return '&per_page={}'.format(per_page)


class IncompleteResultsError(Exception):
    pass


class RequestCounter:
    def __init__(self, timeout=DEFAULT_TIMEOUT_IN_SECONDS):
        self.timeout_in_seconds = timeout  # timeout in seconds
        self.counter = list()

    def append(self, request_time):
        if len(self.counter) < NUMBER_OF_REQUESTS_ALLOWED_PER_MINUTE:
            self.counter.append(request_time)
        else:
            delta = request_time - self.counter[0]
            if delta.seconds < self.timeout_in_seconds:
                print(
                    'Maximum requests "{}" reached'
                    ' timing out for {} seconds.'
                    .format(
                        len(self.counter),
                        self.timeout_in_seconds - delta.seconds
                    )
                )
                self.timeout(self.timeout_in_seconds - delta.seconds)
                self.counter.pop(0)  # pop index 0
                self.counter.append(datetime.now())
            else:
                self.counter.pop(0)  # pop index 0
                self.counter.append(request_time)

    def timeout(self, time_in_seconds=DEFAULT_TIMEOUT_IN_SECONDS):
        time.sleep(time_in_seconds)


class Search(metaclass=ABCMeta):
    request_counter = RequestCounter()

    def __init__(self, query):
        self.total_count = None
        self.incomplete_results = None
        self.results = list()
        self._request(query.query_string)

    def _request(self, query_string):
        Search.request_counter.append(datetime.now())

        print('Making request: {}'.format(query_string))

        headers = {'Authorization': 'token ' + GITHUB_OAUTH_TOKEN}
        r = requests.get(query_string, headers=headers)

        response_body = r.json()

        if r.status_code != 200:
            print('Bad request:')
            print(r.status_code)
            print(response_body)
            Search.request_counter.timeout()
            self._request(query_string)
            return

        self.total_count = response_body['total_count']
        print('Number of results: {}.'.format(self.total_count))
        self.incomplete_results = response_body['incomplete_results']
        if self.incomplete_results:
            raise IncompleteResultsError()
        self.parse_results(response_body['items'])

    @abstractmethod
    def parse_results(self, json_results):
        pass


class SearchRepo(Search):
    def parse_results(self, json_results):
        for item in json_results:
            self.results.append(Repo(item))


class SearchCode(Search):
    def parse_results(self, json_results):
        for item in json_results:
            self.results.append(File(item))


class File:
    def __init__(self, item):
        self.name = item['name']
        self.repo = Repo(item['repository'])


class Repo:
    def __init__(self, item):
        self.url = item['html_url']
        self.name = item['full_name']


def get_dates(
    start_date,
    end_date=date.today()
):
    interval = 7
    delta = end_date - start_date
    for i in range((delta.days // interval) + 1):
        yield (
            start_date + timedelta(days=i * interval),
            start_date + timedelta(days=i * interval + interval)
        )


def analyse_repo(
    args,
    github_repo,
    ui_mode
):
    directory = os.path.dirname(github_repo.path)
    project_modules = get_modules(directory)
    local_modules = get_directory_modules(directory)
    tree = generate_ast(github_repo.path)
    cfg = make_cfg(
        tree,
        project_modules,
        local_modules,
        github_repo.path
    )
    cfg_list = list(cfg)

    initialize_constraint_table(cfg_list)
    analyse(cfg_list)
    vulnerabilities = find_vulnerabilities(
        cfg_list,
        ui_mode,
        VulnerabilityFiles(
            args.blackbox_mapping_file,
            args.trigger_word_file
        )
    )
    return vulnerabilities


def scan_github(
    cmd_line_args,
    ui_mode
):
    for range_start, range_end in get_dates(cmd_line_args.start_date):
        query = Query(
            SEARCH_REPO_URL,
            cmd_line_args.search_string,
            time_interval='{} .. {}'.format(
                range_start,
                range_end
            ),
            per_page=100
        )
        search_repos = SearchRepo(query)
        for repo in search_repos.results:
            query = Query(
                SEARCH_CODE_URL,
                'app = Flask(__name__)',
                repo
            )
            search_code = SearchCode(query)
            if search_code.results:
                repo = repo_runner.Repo(repo.url)
                try:
                    repo.clone()
                except NoEntryPathError as err:
                    print('NoEntryPathError for {}'.format(repo.url))
                    continue
                vulnerabilities = analyse_repo(
                    cmd_line_args,
                    repo,
                    ui_mode
                )
                with open(repo.path + '.pyt', 'a') as fd:
                    if cmd_line_args.json:
                        json.report(vulnerabilities, fd)
                    else:
                        text.report(vulnerabilities, fd)

                if vulnerabilities:
                    add_repo_to_csv(cmd_line_args.csv_path, repo)
                repo.clean_up()


def analyse_repos(cmd_line_args, ui_mode):
    repos = get_repos(cmd_line_args.git_repos)
    for repo in repos:
        repo.clone()
        vulnerabilities = analyse_repo(
            cmd_line_args,
            repo,
            ui_mode
        )
        if cmd_line_args.json:
            json.report(vulnerabilities, sys.stdout)
        else:
            text.report(vulnerabilities, sys.stdout)
        if not vulnerabilities:
            repo.clean_up()
