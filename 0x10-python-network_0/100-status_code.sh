#!/bin/bash
# displays only status code of response by setting output to null & writing out http_code
curl "$1" -so /dev/null -w "%{http_code}"
