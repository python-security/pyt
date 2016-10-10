from abc import abstractmethod, ABCMeta
import re

import requests

GITHUB_API_URL = 'https://api.github.com'
SEARCH_REPO_URL = GITHUB_API_URL + '/search/repositories'
SEARCH_CODE_URL = GITHUB_API_URL + '/search/code'


class Languages:
    _prefix = 'language:'
    python = _prefix + 'python'
    javascript = 'javascript'
    # add others here


class Query:
    def __init__(self, base_url, query_string,
                 language=None, repo=None, time_interval=None):
        repo = self._repo_parameter(repo)
        time_interval = self._time_interval_parameter(time_interval)
        parameters = self._construct_parameters([query_string,
                                                 language,
                                                 repo,
                                                 time_interval])
        self.query_string = self._construct_query(base_url, parameters)

    def _construct_query(self, base_url, parameters):
        query = base_url
        query += '?q='
        query += '+'.join(parameters)
        return query

    def _construct_parameters(self, parameters):
        r = list()
        for p in parameters:
            if p:
                r.append(p)
        return r

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


class Search(metaclass=ABCMeta):
    def __init__(self, query):
        self.total_count = None
        self.incomplete_results = None
        self.items = list()
        self._request(query.query_string)

    def _request(self, query_string):
        r = requests.get(query_string)
        json = r.json()
        #print(query_string)
        #import pprint
        #pprint.pprint(json)
        self.total_count = json['total_count']
        self.incomplete_results = json['incomplete_results']
        self.parse_items(json['items'])

    @abstractmethod
    def parse_items(self, json_items):
        pass


class SearchRepo(Search):
    def parse_items(self, json_items):
        for item in json_items:
            self.items.append(Repo(item))


class SearchCode(Search):
    def parse_items(self, json_items):
        for item in json_items:
            self.items.append(File(item))


class File:
    def __init__(self, json):
        self.name = json['name']
        self.repo = Repo(json['repository'])


class Repo:
    def __init__(self, json):
        self.URL = json['html_url']
        self.name = json['full_name']


if __name__ == '__main__':
    q = Query(SEARCH_REPO_URL, 'flask', time_interval='2010-05-01 .. 2011-01-01')
    print(q.query_string)
    s = SearchRepo(q)
    print(s.total_count)
    print(s.incomplete_results)
    print([r.URL for r in s.items])
    q = Query(SEARCH_CODE_URL, 'import flask', Languages.python, s.items[0])
    s = SearchCode(q)
    print(s.total_count)
    print(s.incomplete_results)
    print([f.name for f in s.items])
