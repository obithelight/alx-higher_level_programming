#!/usr/bin/python3
'''Fetches a url using urllib'''
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        file = response.read()
    print("Body response:")
    print(f"\t- type: {type(file)}")
    print(f"\t- content: {file}")
    print(f"\t- utf8 content: {file.decode('utf-8')}")
