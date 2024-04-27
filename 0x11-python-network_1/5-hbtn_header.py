#!/usr/bin/python3
'''takes in URL, sends a request to it, displays value of the X-Request-Id'''
import sys
import requests


if __name__ == "__main__":
    url = requests.get(sys.argv[1])
    print(url.headers["X-Request-Id"])
