#!/usr/bin/env bash
#script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sX "Delete" "$1"
