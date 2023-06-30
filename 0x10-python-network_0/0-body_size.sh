#!/bin/bash
# script takes a URL as input, sends a request to that URL using curl,
#   and displays the size of the response body in bytes

URL="$1"

# send a request to the URL and store the response in a temporary file
response=$(mktemp)
curl -sI "$URL" -o "$response"

# extract the content length from the response headers
content_length=$(grep -i 'Content-Length' "$response" | awk '{print $2}')

echo "$content_length"

# cleanup temporary file
rm "$response"
