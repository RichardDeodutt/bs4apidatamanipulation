#!/bin/bash

#Richard Deodutt
#09/15/2022
#This script is meant to install everything the programs need as in the dependencies
#Requires Python, Bash, cURL, jq, Python Modules: subprocess, json, os, pycountry

Root='/home/ubuntu/'

Log="$Root""Install.log"

Pathofvenv="$Root""venv"

#Run as admin only check
if [ $UID != 0 ]; then
    echo "Run again with admin permissions" >> $Log
    exit 1
fi

#Update local repo database
apt-get update

#Install python3, pip then venv then git if it not installed
apt-get install python3 -y && echo "Python3 is Installed" >> $Log && apt-get install python3-pip -y && echo "Python pip is Installed" >> $Log && apt-get install python3.10-venv -y && echo "Python venv is Installed" >> Log && apt-get install git -y && echo "Git is Installed" >> $Log

#Install curl and jq if it not installed
apt-get curl -y && echo "Curl is Installed" >> $Log && apt-get install jq -y && echo "Jq is Installed" >> $Log

#Install pip venv enviormentent
python3 -m venv $Pathofvenv && echo "Python venv Directory is Installed" >> $Log

#Activate the venv
source $Pathofvenv"/bin/activate" && echo "Python venv Activated" >> $Log

#Install Flask and pycountry 
pip install flask && echo "Flask is Installed" >> $Log && pip install pycountry && echo "Pycountry is Installed" >> $Log

#Install Gunicorn
pip install gunicorn && echo "Gunicorn is Installed" >> $Log

#Deactivate the venv
deactivate && echo "Python venv Deactivated" >> $Log

#Copy the run script to bin
cp "$Pathofvenv/"run-app.sh /bin/run-app.sh && echo "Script 'run-app.sh' Installed" >> $Log

#Chmod the script to Executable
chmod +x /bin/run-app.sh && echo "Script 'run-app.sh' Executable" >> $Log

#Copy the systemd service to the rest of the services
cp "$Pathofvenv/"run-app.service /etc/systemd/system/run-app.service && echo "Service 'run-app.service' Installed" >> $Log

#Enable the service
systemctl enable run-app && echo "Service 'run-app.service' Enabled" >> $Log

#Start the service
systemctl start run-app && echo "Service 'run-app.service' Started" >> $Log

#Successful
echo "Installation Successful" >> $Log
exit 0