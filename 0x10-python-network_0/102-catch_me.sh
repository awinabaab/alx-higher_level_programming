#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with message containing `You got me!`, in the body of the response
curl -sLX PUT 0:5000/catch_me -H "Origin: School" -d "user_id=98"
