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
    commits = r.json()

    for mycommit in commits[:10]:
        mysha = mycommit.get('sha')
        myauthor = mycommit.get('commit').get('author').get('name')
        print(f"{mysha}: {myauthor}")
