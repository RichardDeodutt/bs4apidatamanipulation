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

`getbored` can be piped to `csvbored.sh`

Example:

`./getbored.sh | ./csvbored.sh`

`main.py` is the interactive CLI

I have 3 bash scripts that are almost the same `getgender`, `getage` and `getnationality`. This is because I want them to be their own individual scripts that can run individually without having to put in the url as a parameter. I suppose I could make them take in a `-g` for gender, `-a` for age, `-n` for nationality and default to `-g` but that may take some time to figure out so I'll leave that for last if I have time. 

# Todo

1. Flask App(Html,CSS,Javascript)(Bootstrap)
2. Install Script
3. Run Script
4. Systemd Service Script
5. Deployment Script
6. Condense the 3 Bash Scripts(Optional)
7. Add more APIs(Optional)
8. More Documentation(Optional)

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