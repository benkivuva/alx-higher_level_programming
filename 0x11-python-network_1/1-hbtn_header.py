#!/usr/bin/python3
"""
This script takes a URL as input, sends an HTTP GET request to the URL,
and displays the value of the 'X-Request-Id' variable from the response header.
"""


import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(dict(response.info()).get('X-Request-Id'))
