#!/bin/bash

#Richard Deodutt
#10/04/2022
#This script is meant to gather data from a API that suggests random activities for bored people or predicted information on a person based on their firstname. 
#Requires curl

#Agrugments for the opts selection

#If to use the bored api
bored='false'
#Gender api name
gendername=''
#Age api name
agename=''
#nationality api Name
nationalityname=''

#The options usage
optsusage() {
    printf "Usage: 'b' is for the bored API\n"
    printf "Usage: 'g' is for the gender name API\n"
    printf "Usage: 'a' is for the age name API\n"
    printf "Usage: 'n' is for the nationality name API\n"
}

#In the case no arguments is specified
if [ $# -eq 0 ] ; then
    printf "Specify some arguments\n"
    optsusage ; exit 1
fi

#Check the options and process them
while getopts 'bg:a:n:' flag; do
    case "${flag}" in
        b) bored="true" ;;
        g) gendername="${OPTARG}" ;;
        a) agename="${OPTARG}" ;;
        n) nationalityname="${OPTARG}" ;;
        *) optsusage ; exit 1 ;;
    esac
done

#Url for the api to get a random activity suggestion
BoredUrl='http://www.boredapi.com/api/activity'

#Url for the api to get gender data based on first name
GenderUrl="https://api.genderize.io?name=$gendername"

#Url for the api to get a age data based on first name
AgeUrl="https://api.agify.io?name=$agename"

#Url for the api to get nationality data based on first name
NationalityUrl="https://api.nationalize.io?name=$nationalityname"

#If bored was selected curl the url
if [[ $bored == 'true' ]]; then
    curl -s $BoredUrl
    if [ $? -ne 0 ]; then
        #Exit error something was wrong with the curl command
        printf "Can't get a random activity\n"
        exit 1
    fi
fi

#If gender name was selected curl the url
if [ -n "$gendername" ]; then
    curl -s $GenderUrl
    if [ $? -ne 0 ]; then
        #Exit error something was wrong with the curl command
        printf "Can't get the gender from name\n"
        exit 1
    fi
fi

#If age name was selected curl the url
if [ -n "$agename" ]; then
    curl -s $AgeUrl
    if [ $? -ne 0 ]; then
        #Exit error something was wrong with the curl command
        printf "Can't get the age from name\n"
        exit 1
    fi
fi

#If nationality name was selected curl the url
if [ -n "$nationalityname" ]; then
    curl -s $NationalityUrl
    if [ $? -ne 0 ]; then
        #Exit error something was wrong with the curl command
        printf "Can't get the nationality from name\n"
        exit 1
    fi
fi

#Exit success
exit 0