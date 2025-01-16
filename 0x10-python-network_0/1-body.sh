#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays only the body of a 200 status response
curl -sL "$1"
