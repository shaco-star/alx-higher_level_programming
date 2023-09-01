#!/usr/bin/python3

"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

if __name__ == "__main__":
    import requests
    import sys

    repo_name = sys.argv[1]
    user_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'
    .format(user_name, repo_name)
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            print("{}: {}".format(commit.get('sha'),
                                  commit.get('commit')
                                  .get('author')
                                  .get('name')))
