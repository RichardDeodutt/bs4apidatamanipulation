#!/bin/bash

#Richard Deodutt
#09/15/2022
#This script is meant to deploy the whole app when put in a ec2 userdata for the creation. Port is 80 so no port and it should be http
#Requires Python, Bash, cURL, jq, Python Modules: subprocess, json, os, pycountry

Root='/home/ubuntu/'

Log="$Root""Deploy.log"

Pathofvenv="$Root""venv"

#Run as admin only check
if [ $UID != 0 ]; then
    echo "Run again with admin permissions" >> $Log
    exit 1
fi


#Install Git
apt-get install git -y && echo "Git is Installed" >> $Log

#Clone the Repo
cd $Root && git clone https://github.com/RichardDeodutt/bs4apidatamanipulation.git && mv "$Root""bs4apidatamanipulation" "$Root""venv" && echo "Cloned Repo" >> $Log

#Change directory in to the cloned repo and run the install script and change directory back out
cd "$Root""venv" && /bin/bash install.sh && cd .. && echo "Ran 'install.sh'" >> $Log

#Log Installation Complete
echo "Installation Complete" >> $Log

#Delay for 10 seconds for it to load
sleep 10

#Install Screenfetch
apt-get install screenfetch -y && echo "Installed Screenfetch" >> $Log
#Log url-shortener Status
echo "$(echo ; systemctl status url-shortener --no-pager)" >> $Log
#Log Screenfetch
echo "$(echo ; screenfetch)" >> $Log

#Successful
echo "Installation Successful" >> $Log
exit 0