#!/usr/bin/python3
"""Takes in a URL as a command line argument,
sends a request to the URL and displays the body of the response"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    request = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            content = response.read()
            print(f"{content.decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.status}")
