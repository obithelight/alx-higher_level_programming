#!/usr/bin/python3
'''
Python script that evaluates candidates applying
for a back-end position with multiple technical challenges
'''
import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/obithelight/printf/commits'

    r = requests.get(url)
    total_commits = r.json()

    for each_commit in total_commits[:10]:
        sha = each_commit.get('sha')
        author = each_commit.get("commit").get("author").get("name")
        print(f"{sha}: {author}")
