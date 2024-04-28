#!/usr/bin/python3
'''
Python script that evaluates candidates applying
for a back-end position with multiple technical challenges
'''
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/obithelight/printf/commits'

    r = requests.get(url)
    commits = r.json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")
