#!/bin/bash
# that causes the server to respond with a message
curl  -sLH "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me -X PUT -d "user_id=98"
