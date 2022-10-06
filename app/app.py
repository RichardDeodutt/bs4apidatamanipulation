#!/usr/bin/python3

#Richard Deodutt
#09/15/2022
#This script is meant to gather data from a API and organize that data into a csv file using Python and Bash. This is the Flask app.
#Issues

#Import Flask
from flask import Flask, send_file, jsonify, request

#Import the main.py CLI
import cli.main

#Import json for working with JSON
import json

#Flask app name
app = Flask(__name__)

#Takes JSON Input and converts it to CSV and returns it, This is probably not secure
@app.route('/jsontocsv', methods=['POST'])
def postjsontocsv():
    #Try the below code and if it fails return a error
    try:
        #This is the user input JSON
        InputData = request.get_json()
        #Load the JSON string to a dict
        InputJSON = json.loads(InputData)
    except:
        return "This JSON is not valid, can't continue", 400
    #This is the converted CSV
    OutputCSV = main.JSONtoCSV(InputJSON)
    #Return the CSV
    return OutputCSV

#Calls the bored function to query the bored api for a random activity
@app.route('/bored', methods=['GET'])
def getbored():
    #Call the GetBored function that calls the api
    BoredData = main.GetBored()
    #Load the JSON string to a dict
    BoredJSON = json.loads(BoredData)
    #Convert the json to a pretty json
    PrettyJSON = main.PrettyBored(BoredJSON)
    #Return the pretty json
    return json.dumps(PrettyJSON)

#Calls the name function to query the name apis for data
@app.route('/name/<name>', methods=['GET'])
def getname(name):
    if name == "" or not all(Character.isalpha() for Character in name):
        #Name is not valid so tell user
        return "This first name is not valid, can't continue", 400
    #Call the GetName function that calls the api
    NameJSON = main.GetName(name)
    #Convert the json to a pretty json
    PrettyJSON = main.PrettyName(NameJSON)
    #Return the pretty json
    return json.dumps(PrettyJSON)

#Home page at the root
@app.route('/', methods=['GET'])
def getindex():
    #Send the index.html file
    return send_file('index.html')