#!/usr/bin/python3

"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.request as request
    import urllib.error as error
    import sys

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
