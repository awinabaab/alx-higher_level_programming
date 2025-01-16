#!/bin/bash
# Takes in a URL, sends a DELETE request to the URL, and displays only the body of the response
curl -sX DELETE "$1"
