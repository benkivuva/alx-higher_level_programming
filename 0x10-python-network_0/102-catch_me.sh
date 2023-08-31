#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -X PUT -d "user_id=98" --header "Origin: School" -sL 0:5000/catch_me
