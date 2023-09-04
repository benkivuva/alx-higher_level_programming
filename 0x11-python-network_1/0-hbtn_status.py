#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status
and displays the response body.
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
        'https://alx-intranet.hbtn.io/status'
    ) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format(html.__class__, html, html.decode('utf-8')))
