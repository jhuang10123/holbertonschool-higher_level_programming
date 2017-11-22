#!/bin/bash
# sends a GET request to URL and displays the body of the response
curl "$1" -sH "X-HolbertonSchool-User-Id: 98" -X GET
