#!/usr/bin/python3
"""Takes in a URL and an email address from the command line,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    data = {"email": argv[2]}

    response = requests.post(url, data=data)
    print(response.text)
