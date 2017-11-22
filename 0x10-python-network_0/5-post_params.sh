#!/bin/bash
# sends a POST request to URL and displays the body of the response
curl "$1" -sd email=hr@holbertonschool.com -d subject="I will always be here for PLD"
