#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the size of the body of the response
curl -s "$1" | wc -c
