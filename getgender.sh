#!/bin/bash

#Richard Deodutt
#09/14/2022
#This script is meant to gather data from a API that predicts the most probable gender using a first name
#Requires curl
#Issues

#First argument is the first name to use, overrides pipe if it's set
if [ -n "$1" ]; then
    #Argument was passed so use that
    Data=$1
#Argument was not passed so use pipe if it's set
else
    #Check if stdin or pipe is empty
    if [ -t 0 ]; then
        #Pipe is open means there is no input to get, no argument passed or pipe means exit error
        exit 1
    else
        #Pipe is closed means that there is input to get so cat it
        Data=$(cat)
    fi
fi

#Url for the api to get a random activity suggestion
Url="https://api.genderize.io?name=$Data"

#Curl the api sending output to stdout
curl -s $Url

if [ $? -ne 0 ]; then
    #Exit error something was wrong with the curl command
    exit 1
fi

#Exit success
exit 0