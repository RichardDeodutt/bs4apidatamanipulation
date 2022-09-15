#!/bin/bash

#Richard Deodutt
#09/13/2022
#This script is meant to convert json data into a csv format using jq.
#Requires jq
#Issues

#First argument is the json data to save, overrides pipe if it's set
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

#Use jq to convert the data from JSON to CSV
echo "$Data" | jq -r '. as $Data | . | keys_unsorted as $UKeys | $UKeys as $Colums | map($Data as $Row | $Colums | map($Row[.])) as $Rows | $Colums, $Rows[1] | @csv'

#Exit success
exit 0