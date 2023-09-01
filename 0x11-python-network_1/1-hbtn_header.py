#!/usr/bin/python3

"""sends a request to the URL and displays the value of the X-Request-Id"""

import urllib.request as request
import sys

url = sys.argv[1]
with request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
