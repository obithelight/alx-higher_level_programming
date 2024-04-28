#!/usr/bin/python3
'''takes in a letter, sends POST request to http://0.0.0.0:5000/search_user'''
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        mydata = {'q': ''}
    else:
        mydata = {'q': sys.argv[1]}

    req = requests.post(url, data=mydata)

    try:
        req = req.json()
        if req == {}:
            print("No result")
        else:
            print(f"[{req.get('id')}] {req.get('name')}")

    except ValueError:
        print("Not a valid JSON")
