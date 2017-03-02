import re
import requests
import time
from abc import ABCMeta, abstractmethod
from datetime import date, datetime, timedelta

from . import repo_runner
from .reaching_definitions_taint import ReachingDefinitionsTaintAnalysis
from .repo_runner import add_repo_to_csv, NoEntryPathError
from .save import save_repo_scan
from .vulnerabilities import SinkArgsError


DEFAULT_TIMEOUT_IN_SECONDS = 60
GITHUB_API_URL = 'https://api.github.com'
GITHUB_OAUTH_TOKEN = None
NUMBER_OF_REQUESTS_ALLOWED_PER_MINUTE = 30  # Rate limit is 10 and 30 with auth
SEARCH_CODE_URL = GITHUB_API_URL + '/search/code'
SEARCH_REPO_URL = GITHUB_API_URL + '/search/repositories'


def set_github_api_token():
    global GITHUB_OAUTH_TOKEN
    try:
        GITHUB_OAUTH_TOKEN = open('github_access_token.pyt',
                                  'r').read().strip()
    except FileNotFoundError:
        print('Insert your GitHub access token'
              ' in the github_access_token.pyt file in the pyt package'
              ' if you want to use GitHub search.')
        exit(0)


class Languages:
    _prefix = 'language:'
    python = _prefix + 'python'
    javascript = _prefix + 'javascript'
    # add others here


class Query:
    def __init__(self, base_url, search_string,
                 language=None, repo=None, time_interval=None, per_page=100):
        repo = self._repo_parameter(repo)
        time_interval = self._time_interval_parameter(time_interval)
        search_string = self._search_parameter(search_string)
        per_page = self._per_page_parameter(per_page)
        parameters = self._construct_parameters([search_string,
                                                 language,
                                                 repo,
                                                 time_interval,
                                                 per_page])
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
                print('Maximum requests "{}" reached'
                      ' timing out for {} seconds.'
                      .format(len(self.counter),
                              self.timeout_in_seconds - delta.seconds))
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

        json = r.json()

        if r.status_code != 200:
            print('Bad request:')
            print(r.status_code)
            print(json)
            Search.request_counter.timeout()
            self._request(query_string)
            return

        self.total_count = json['total_count']
        print('Number of results: {}.'.format(self.total_count))
        self.incomplete_results = json['incomplete_results']
        if self.incomplete_results:
            raise IncompleteResultsError()
        self.parse_results(json['items'])

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
    def __init__(self, json):
        self.name = json['name']
        self.repo = Repo(json['repository'])


class Repo:
    def __init__(self, json):
        self.url = json['html_url']
        self.name = json['full_name']


def get_dates(start_date, end_date=date.today(), interval=7):
    delta = end_date - start_date
    for i in range(delta.days // interval):
        yield (start_date + timedelta(days=(i * interval) - interval),
               start_date + timedelta(days=i * interval))
    else:
        # Take care of the remainder of days
        yield (start_date + timedelta(days=i * interval),
               start_date + timedelta(days=i * interval +
                                      interval +
                                      delta.days % interval))


def scan_github(search_string, start_date, analysis_type, analyse_repo_func, csv_path):
    analyse_repo = analyse_repo_func
    for d in get_dates(start_date, interval=7):
        q = Query(SEARCH_REPO_URL, search_string,
                  language=Languages.python,
                  time_interval=str(d[0]) + ' .. ' + str(d[1]),
                  per_page=100)
        s = SearchRepo(q)
        for repo in s.results:
            q = Query(SEARCH_CODE_URL, 'app = Flask(__name__)',
                      Languages.python, repo)
            s = SearchCode(q)
            if s.results:
                r = repo_runner.Repo(repo.url)
                try:
                    r.clone()
                except NoEntryPathError as err:
                    save_repo_scan(repo, r.path, vulnerability_log=None, error=err)
                    continue
                except:
                    save_repo_scan(repo, r.path, vulnerability_log=None, error='Other Error Unknown while cloning :-(')
                    continue
                try:
                    vulnerability_log = analyse_repo(r, analysis_type)
                    if vulnerability_log.vulnerabilities:
                        save_repo_scan(repo, r.path, vulnerability_log)
                        add_repo_to_csv(csv_path, r)
                    else:
                        save_repo_scan(repo, r.path, vulnerability_log=None)
                    r.clean_up()
                except SinkArgsError as err:
                    save_repo_scan(repo, r.path, vulnerability_log=None, error=err)
                except SyntaxError as err:
                    save_repo_scan(repo, r.path, vulnerability_log=None, error=err)
                except IOError as err:
                    save_repo_scan(repo, r.path, vulnerability_log=None, error=err)
                except AttributeError as err:
                    save_repo_scan(repo, r.path, vulnerability_log=None, error=err)
                except:
                    save_repo_scan(repo, r.path, vulnerability_log=None, error='Other Error Unknown :-(')

if __name__ == '__main__':
    for x in get_dates(date(2010, 1, 1), interval=93):
        print(x)
    exit()
    scan_github('flask', ReachingDefinitionsTaintAnalysis)
    exit()
    q = Query(SEARCH_REPO_URL, 'flask')
    s = SearchRepo(q)
    for repo in s.results[:3]:
        q = Query(SEARCH_CODE_URL, 'app = Flask(__name__)', Languages.python, repo)
        s = SearchCode(q)
        r = repo_runner.Repo(repo.url)
        r.clone()
        print(r.path)
        r.clean_up()
        print(repo.name)
        print(len(s.results))
        print([f.name for f in s.results])
    exit()

    r = RequestCounter('test', timeout=2)
    for x in range(15):
        r.append(datetime.now())
    exit()

    dates = get_dates(date(2010, 1, 1))
    for date in dates:
        q = Query(SEARCH_REPO_URL, 'flask',
                  time_interval=str(date) + ' .. ' + str(date))
        print(q.query_string)
    exit()
    s = SearchRepo(q)
    print(s.total_count)
    print(s.incomplete_results)
    print([r.URL for r in s.results])
    q = Query(SEARCH_CODE_URL, 'import flask', Languages.python, s.results[0])
    s = SearchCode(q)
    #print(s.total_count)
    #print(s.incomplete_results)
    #print([f.name for f in s.results])
