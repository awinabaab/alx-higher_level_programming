#!/bin/bash
# Takes in a URL, and displays all the HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep -i "Allow" | cut -d " " -f 2-
