"""This modules runs PyT on a CSV file of git repos."""
import os
import git
import shutil


class Repo:
    """Holder for a repo with git URL and
    a path to where the analysis should start"""
    def __init__(self, URL, path):
        self.URL = URL.strip()
        self.path = path.strip()
        self.directory = None

    def clone(self):
        """Clone repo and update path to match the current one"""
        git.Git().clone(self.URL)

        self.directory = self.URL.split('/')[-1].split('.')[0]

        if self.path[0] == '/':
            self.path = self.path[1:]

        self.path = os.path.join(self.directory, self.path)

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
