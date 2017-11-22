#!/bin/bash
# sends a GET request to URL and displays the body of the response
# header variable X-HolbertonSchool-User-Id=98
curl "$1" -sH "X-HolbertonSchool-User-Id: 98" 
