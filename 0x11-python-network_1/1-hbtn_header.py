#!/usr/bin/python3
"""Takes in a URL as a command line argument, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response."""


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        headers = dict(response.getheaders())
        print(f"{headers.get('X-Request-Id')}")
