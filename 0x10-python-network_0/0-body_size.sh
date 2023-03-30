#!/bin/bash
# Bash script that takes in a URL, 
# sends a request to that URL, 
# and displays the size of the body of the response

url="$1"

tmpfile=$(mktemp)
curl -sSL "$url" -o "$tmpfile"

size=$(wc -c < "$tmpfile")
echo "$size"
rm "$tmpfile"
