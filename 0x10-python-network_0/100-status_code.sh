#!/bin/bash
# Sends request to a URL passed as an argument, and displays only the status code of the response
curl -so /dev/null "$1" -w "%{http_code}"
