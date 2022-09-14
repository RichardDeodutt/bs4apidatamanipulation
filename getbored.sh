#!/bin/bash

#Richard Deodutt
#08/15/2022
#This script is meant to gather data from a API that suggests random activities for bored people.
#Requires curl
#Issues

#Url for the api to get a random activity suggestion
Url='http://www.boredapi.com/api/activity'

#Curl the api sending output to stdout
curl -s $Url

if [ $? -ne 0 ]; then
    #Exit error something was wrong with the curl command
    exit 1
fi

#Exit success
exit 0