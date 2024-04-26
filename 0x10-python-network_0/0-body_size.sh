#!/bin/bash
# script that takes in URL and displays the size of the body of the response
curl -sI $1 | grep Content-Length | cut -d " " -f 2
