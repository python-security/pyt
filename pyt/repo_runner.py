"""Runs PyT on a CSV file of git repos."""
import os
import shutil

import git


DEFAULT_CSV_PATH = 'flask_open_source_apps.csv'


class NoEntryPathError(Exception):
    pass


class Repo:
    """Holder for a repo with git URL and
    a path to where the analysis should start."""

    def __init__(
        self,
        URL,
        path=None
    ):
        self.URL = URL.strip()
        self.directory = None
        self.path = path.strip() if path else None

    def clone(self):
        """Clone repo and update path to match the current one."""

        repo = self.URL.split('/')[-1].split('.')
        if len(repo) > 1:
            self.directory = '.'.join(repo[:-1])
        else:
            self.directory = repo[0]

        if self.directory not in os.listdir():
            git.Git().clone(self.URL)

        if self.path is None:
            self._find_entry_path()
        elif self.path[0] == '/':
            self.path = self.path[1:]
        self.path = os.path.join(self.directory, self.path)

    def _find_entry_path(self):
        for root, dirs, files in os.walk(self.directory):
            for f in files:
                if f.endswith('.py'):
                    with open(os.path.join(root, f), 'r') as fd:
                        if 'app = Flask(__name__)' in fd.read():
                            self.path = os.path.join(root, f)
                            return
        raise NoEntryPathError(
            'No entry path found in repo {}.'
            .format(self.URL)
        )

    def clean_up(self):
        """Deletes the repo"""
        shutil.rmtree(self.directory)


def get_repos(csv_path):
    """Parses a CSV file containing repos."""
    repos = list()
    with open(csv_path, 'r') as fd:
        for line in fd:
            url, path = line.split(',')
            repos.append(Repo(url, path))
    return repos


def add_repo_to_csv(
    repo,
    csv_path=DEFAULT_CSV_PATH
):
    try:
        with open(csv_path, 'a') as fd:
            fd.write(
                '{}{}, {}'.format(
                    os.linesep,
                    repo.URL,
                    repo.path
                )
            )
    except FileNotFoundError:
        print('-csv file not used and fallback path not found: {}'
              .format(DEFAULT_CSV_PATH))
        print('To specify the csv_path '
              'use the "-csv" option.')
        exit(1)
