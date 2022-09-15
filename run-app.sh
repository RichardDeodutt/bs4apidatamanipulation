#!/bin/bash

#Richard Deodutt
#09/15/2022
#This script is meant to run the flask app
#Requires Python, Bash, cURL, jq, Python Modules: subprocess, json, os, pycountry

Root='/home/ubuntu/'

Log="$Root""AppRun.log"

Pathofvenv="$Root""venv"

#Run as admin only check
if [ $UID != 0 ]; then
    echo "Run again with admin permissions" >> $Log
    exit 1
fi

#Activate the venv
source $Pathofvenv"/bin/activate" && echo "Python venv Activated" >> $Log

#Run the Flask App
cd $Pathofvenv && gunicorn --bind 0.0.0.0:80 app:app && cd .. && echo "Ran App" >> $Log

#Deactivate the venv
deactivate && echo "Python venv Deactivated" >> $Log

#Successful
echo "Run Successful" >> $Log
exit 0