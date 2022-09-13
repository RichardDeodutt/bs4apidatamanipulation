#!/bin/bash

#Richard Deodutt
#08/15/2022
#This script is meant to save gathered data from a API that suggests random activities for bored people into a csv file.
#Requires jq
#Issues

#First argument is the json data to save
Data=$1

#Use jq to convert the data from JSON to CSV
echo "$Data" | jq -r '. as $Data | . | keys_unsorted as $UKeys | $UKeys as $Colums | map($Data as $Row | $Colums | map($Row[.])) as $Rows | $Colums, $Rows[1] | @csv'