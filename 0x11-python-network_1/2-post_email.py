#!/usr/bin/python3
"""Takes in a URL and an email as comman line arguments,
sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')

    request = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print(f"{content.decode('utf-8')}")
