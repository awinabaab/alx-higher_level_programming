#!/usr/bin/python3
"""Takes in a letter from the command line and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""


if __name__ == "__main__":
    import requests
    from sys import argv

    q = ""
    if len(argv) > 1 and argv[1]:
        q = argv[1]

    params = {"q": q}
    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, params)
    if response.headers.get('Content-Type') == 'application/json':
        json_content = response.json()
        if json_content:
            print(f"[{json_content.get('id')}] {json_content.get('name')}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
