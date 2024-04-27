#!/usr/bin/python3
'''takes in a URL, sends a request to it and displays the X-Request-Id'''

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.headers.get("X-Request-Id")
        print(html)
