#!/usr/bin/python3
'''
Lists the 10 recent commits in a GitHub repository and the committers
'''
import sys
import requests


if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    r = requests.get(url)

    commit_history = r.json()

    for each_commit in commit_history[:10]:
        sha = each_commit.get('sha')
        committer = each_commit.get('commit').get('author').get('name')
        print(f'{sha}: {committer}')
