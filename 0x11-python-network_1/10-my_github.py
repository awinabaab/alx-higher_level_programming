#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""


if __name__ == "__main__":
    import requests
    from sys import argv

    user = argv[1]
    pwd = argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(user, pwd))
    json_content = response.json()
    print(json_content.get('id'))
