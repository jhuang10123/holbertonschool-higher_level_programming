#!/bin/bash
# sends a POST request to URL and displays the body of the response
# email = hr@holbertonschool.com
# subject = "I will always be here for PLD"
curl "$1" -sd email=hr@holbertonschool.com -d subject="I will always be here for PLD"
