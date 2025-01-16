#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
