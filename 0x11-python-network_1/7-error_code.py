#!/usr/bin/python3
"""Takes in a URL from the command line,
sends a request to the URL and displays the body of the response"""


if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.get(argv[1])
    status = response.status_code

    if status >= 400:
        print(f"Error code: {status}")
        exit(1)

    print(response.text)
