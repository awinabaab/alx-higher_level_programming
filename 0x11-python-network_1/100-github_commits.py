#!/usr/bin/python3
"""Takes two arguments, owner name and respository name,
and List 10 commits (from the most recent to oldest) of the repository"""


if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)
    commits = response.json()[:10]

    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
