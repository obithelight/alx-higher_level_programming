#!/usr/bin/python3
'''takes in a URL, sends a request it and displays the value of X-Request-Id'''
import sys
import requests


if __name__ == "__main__":
    url = requests.get(sys.argv[1])
    print(url.headers['X-Request-Id'])
