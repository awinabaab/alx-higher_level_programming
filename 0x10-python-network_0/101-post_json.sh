#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, and displays the response of the body
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
