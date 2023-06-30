#!/bin/bash
# curl for Content-Length of the response body in bytes
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
