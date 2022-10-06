# bs4apidatamanipulation

## Build Script 4 Api Data Manipulation

### Objective: 

Demonstrate your ability to gather data from an API and organize that data into a specific format. 

Create a script that uses Bash and Python to interact with any API (Some API’s will require authentication). 

### Requirements: 

1. Create a CSV file of the data you choose to store in the file. 
2. Only 6 columns are required for this activity (e.g. of the MLB API: Player’s name, number, team, position, height and weight). 
3. The script can be interactive or not interactive (You can allow a user to pick a or some parameter). 
4. CSV file must be formatted properly. 

Please submit your GitHub link of your script. 

Take away: After creating your script, you will have the ability to access data from an API and format that data into a specific format; to share amongst other teams or software that can ingest that data. 

## Heading: 

```
#Name
#Date
#Description
#Instructions and Issues
```

# Notes

[main.py](https://github.com/RichardDeodutt/bs4apidatamanipulation/blob/main/app/cli/main.py) is the interactive CLI. This uses bash [scripts](https://github.com/RichardDeodutt/bs4apidatamanipulation/tree/main/app/cli/scripts) to access third party apis. 

[app.py](https://github.com/RichardDeodutt/bs4apidatamanipulation/blob/main/app/app.py) is the flask app. This uses [main.py](https://github.com/RichardDeodutt/bs4apidatamanipulation/blob/main/app/cli/main.py) as a module. 

[deployment.sh](https://github.com/RichardDeodutt/bs4apidatamanipulation/blob/main/deployment.sh) is the script to deploy the flask app to a AWS EC2. 

Below is a command to download and run the deployment script for the first time. 
```
cd && curl -s -O https://raw.githubusercontent.com/RichardDeodutt/bs4apidatamanipulation/main/deployment.sh && sudo chmod +x deployment.sh && sudo ./deployment.sh
```

Below is a command to download and run the deployment script for after the first time. 
```
cd && sudo rm -r venv ; curl -s -O https://raw.githubusercontent.com/RichardDeodutt/bs4apidatamanipulation/main/deployment.sh && sudo chmod +x deployment.sh && sudo ./deployment.sh
```

# Dependencies:

1. [Python](https://www.python.org/)
2. [Bash](https://www.gnu.org/software/bash/)
4. [cURL](https://curl.se/)
3. [jq](https://stedolan.github.io/jq/)

# Python Modules:

1. [subprocess](https://docs.python.org/3/library/subprocess.html)
2. [json](https://docs.python.org/3/library/json.html)
3. [os](https://docs.python.org/3/library/os.html)
4. [pycountry](https://pypi.org/project/pycountry/)

# 3rd Party APIs:
1. [The Bored API](https://www.boredapi.com/)
2. **The Name APIs**
    - [Gender](https://genderize.io/)
    - [Age](https://agify.io/)
    - [Nationality](https://nationalize.io/)