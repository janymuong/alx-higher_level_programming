#!/bin/bash
# script takes a URL as input, sends a request to that URL using curl,
#   and displays the size of the response body in bytes

URL="$1"

# send a request to the URL
response=$(curl -sI "$URL")

# extract the content length from the response headers
echo "$response" | grep -i 'Content-Length' | awk '{print $2}'
