#!/usr/bin/python3

"""
 script that takes in a letter and sends a
 POST request to http://0.0.0.0:5000/search_user
 with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys

    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}
    response = requests.post(url, data=data)
    try:
        response_json = response.json()
        if not response_json:
            print("No result")
        else:
            print("[{}] {}".format(response_json["id"], response_json["name"]))
    except ValueError:
        print("Not a valid JSON")
