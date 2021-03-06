import requests
import logging
from traceback import format_exc
from datetime import datetime


log = logging.getLogger(__name__)

def fetch_commits(repo_name):
    """
    Cached commits from GitHub API

    :return:    JSON with commits api
    """
    try:
        r = requests.get('https://api.github.com/repos/iScrE4m/{}/commits'.format(repo_name))
    except requests.exceptions.ConnectionError:
        log.error("Connection error when connecting to Github: %s", format_exc())
        return None
    if r.status_code != 200:
        log.error("Bad status code from Github, got %s", r.status_code)
        return None
    return r.json()


class Commits:
    """
    Object holding information about a commit, called with name of a repository

    Get commit information by calling Commits.list[x].var
    x = 0 will get the newest and 14 the oldest
    """

    def __init__(self, repo_name):
        self.commits = fetch_commits(repo_name)
        self.list = [self.parse_commit(x) for x in range(0, 15)]

    def parse_commit(self, number):
        if self.commits is None:
            return Commit("2037-07-31T00:00:00Z", "Error parsing commit - may be caused by Github connection issues",
                          faulty=True)
        try:
            date = self.commits[number]['commit']['author']['date']
            message = self.commits[number]['commit']['message']
        except (IndexError, TypeError, KeyError):
            log.error("Exception happened while parsing commits: %s", format_exc())
            return Commit("2037-07-31T00:00:00Z", "Error parsing commit - may be caused by Github connection issues",
                          faulty=True)
        return Commit(date, message)


class Commit:
    """
    Information about a commit

    self.date       string with date like 2016-07-12T19:26:15Z
    self.datetime   datetime object
    self.message    commit message
    """

    def __init__(self, date, message, faulty=False):
        self.date = date
        self.datetime = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        self.message = message
        self.faulty = faulty
