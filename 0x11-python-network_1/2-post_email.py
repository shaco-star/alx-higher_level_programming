#!/usr/bin/python3

"""
sends a request to the URL and displays the value of the X-Request-Id
"""
import urllib.parse

if __name__ == "__main__":
    import urllib.request as request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
