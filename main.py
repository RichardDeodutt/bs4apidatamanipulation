#!/usr/bin/python3

#Richard Deodutt
#09/13/2022
#This script is meant to gather data from a API and organize that data into a csv file using Python and Bash.
#Requires curl and jq
#Issues

#Subprocess to run bash scripts
import subprocess

#Neede to convert the api data to usable format
import json

#Exists function to check if a file exists already
from os.path import exists

#Yes or no Prompt
def YNPromt(Prompt):
    #Get the user input
    UserInput=input(Prompt+" Y/N: ")
    #If user just pressed enter and inputs nothing assume yes
    if UserInput == "":
        #Yes so return true
        return True
    #Check if it starts with a 'y' if it does assume yes
    if UserInput[0].lower() == "y":
        #Yes so return true
        return True
    #Check if it starts with a 'n' if it does assume no
    elif UserInput[0].lower() == "n":
        #No so return false
        return False
    #If the user entered something else assume no
    else:
        #Tell the user they are not understood
        print("Did not understand that assuming no.")
        #No so return false
        return False

#Function to give a user a prompt and a list of options to select using a number. Options must be a dictionary
def Pick(Prompt, Options):
    #Print the prompt
    print(Prompt)
    #Loops throught the list of items
    for Index, Item in enumerate(Options):
        #Prints the current index offset by 1 and the current item from the list
        print(str(Index+1)+'. '+Item)
    #Get the users selection
    UserInput = input("#> ")
    try:
        #Convert input to int
        UserSelection=int(UserInput)
    except:
        #User entered something that is not a int so assume they picked the first
        print("I didn't understand that so lets go with the first one")
        UserSelection = 1
    #Remove 1 to correct it because indexs start at 0
    UserSelection-=1
    #If user selected out of bounds pick the first thing but if it's okay return their selection
    if UserSelection > len(Options)-1 or UserSelection < 0:
        #Select the first thing
        print("Your selection does not seem right let me pick for you then")
        #Convert the keys to a list and select the the first key using the index 0 in the list and return the key
        return list(Options.keys())[0]
    else:
        #Convert the dictonary keys to a list and select the the key using the index the user selected in the list and return the key
        return list(Options.keys())[UserSelection]

#Welcome the user and get some information from them if needed
def Welcome():
    #Welcome message, API Data Manipulation
    print("Welcome to a ADM")
    return None

#Exits the program
def Exit():
    #Confirm the user wants to exit
    if not YNPromt('Are you sure you want to exit?'):
        return None
    #Goodbye message
    print("Exiting. Goodbye")
    #Exit success
    exit(0)

#Print RAW JSON data
def PrintRAWJSON(JSON):
    print(JSON)
    #Return self
    return PrintRAWJSON

#Print JSON Data
def PrintJSON(JSON):
    #Print out all the keys and values from the JSON
    for Item in JSON:
        #Capitalize the keys and values unless it's a http link or number
        if isinstance(JSON[Item], str) and 'http' not in JSON[Item]:
            #Not a number or http link
            print(Item.capitalize()+':', "'"+str(JSON[Item]).capitalize()+"'")
        else:
            #Number or contains 'http'
            print(Item.capitalize()+':', "'"+str(JSON[Item])+"'")
    #Return self
    return PrintJSON

def CSVBored(JSON):
    return subprocess.run(['./csvbored.sh', json.dumps(JSON)], capture_output=True, text=True).stdout

#Save Bored JSON to CSV file
def SavetoBoredCSV(JSON):
    #Tell the user what we will do
    print('Saving Bored Data to Bored.csv')
    #Convert Bored JSON to CSV
    CSVData = CSVBored(JSON)
    #If the file does not exist write to file with the headers
    if not exists('bored.csv'):
        #Append to the bored.csv file
        with open('bored.csv', 'a') as File:
            #Print the data being written
            print(CSVData)
            #Write with the headers to the file
            File.write(CSVData)
    else:
        #File already exists append to bored.csv file only the data no header
        with open('bored.csv', 'a') as File:
            #Print only the data being written no header
            print(CSVData.splitlines()[1])
            #Write the data only no headers to file
            File.write(CSVData.splitlines()[1]+'\n')
    #Save completed
    print('Saved Bored Data to Bored.csv')
    #Return another function so this can't be called for the same data
    #This is not the best or foolproof method to stop duplicate data but it's better than nothing
    return AlreadySavedtoBoredCSV

#Tell the user Bored JSON was saved to CSV file
def AlreadySavedtoBoredCSV(JSON):
    #Tell the user the bored data was already saved to csv
    print('Already saved Bored data to Bored.csv')
    #Return self
    return AlreadySavedtoBoredCSV

def PrintBoredJSON(JSON):
    #Print Activity
    print('Activity:', JSON['activity'].capitalize()+'.')
    #Print Type
    print('Type:', JSON['type'].capitalize())
    #Print Participants
    print('Participants:', JSON['participants'])
    #Print Price
    print('Price:', str(round(JSON['price'] * 10, 1))+'/10')
    #Print Accessibility
    print('Accessibility:', str(round(JSON['accessibility'] * 10, 1))+'/10')
    #Print Link if it's not blank
    if JSON['link'] != "":
        print('Link:', JSON['link'])
    #Return self
    return PrintBoredJSON

def GetBored():
    return subprocess.run(['./getbored.sh'], capture_output=True, text=True).stdout

#User is bored so get them a random activity suggestion
def Bored():
    #Tell the user what we will do
    print('Let me suggest a random activity you can do then!')
    #Subprocess call to the bash script to get a random activity suggestion using a api and curl
    ActivityData = GetBored()
    #Convert the string into a dictionary using json
    ActivityJSON = json.loads(ActivityData)
    #Print out the data for the user to see their random activity suggestion
    print('Your Random Activity is as Follows: ')
    #Print out bored api data
    PrintBoredJSON(ActivityJSON)
    #Options on what to do with this data
    Options = { "Print Bored Data": PrintBoredJSON, "Print All Bored Data": PrintJSON, "Print Raw Bored Data": PrintRAWJSON, 'Save to Bored.csv': SavetoBoredCSV, "Go Back": None }
    #Infinite Loop
    while True:
        #Space out text for clarity
        print()
        #Bored Menu
        print('Bored Menu')
        #Get the user selection
        Selection = Pick('What would you like to do?', Options)
        #User wants to go back
        if Options[Selection] is None:
            #Return back and return self
            return Bored
        else:
            #Space out text for clarity
            print()
            #Run the funtion the user selected and pass the JSON data. returning a new function to replace it or with the None type
            Replacement = Options[Selection](ActivityJSON)
            #Replace the function with what it returned
            Options[Selection] = Replacement

#Analayze a first name
def FirstNameAnalyzer():
    #Return self
    return FirstNameAnalyzer

#Main menu of options the user can do
def Menu():
    #Dictionary of options where each entry is a funtion that can be run
    Options = { "I'm Bored": Bored, "Analyze a First Name": FirstNameAnalyzer, "Exit": Exit }
    #Infinte Loop
    while True:
        #Space out text for clarity
        print()
        #Main Menu
        print('Main Menu')
        #Get the users selection
        Selection = Pick('What would you like to do?', Options)
        #Space out text for clarity
        print()
        #Run the funtion the user selected. returning a new function to replace it
        Replacement = Options[Selection]()
        #Replace the function with what it returned
        Options[Selection] = Replacement

#The main program
def main():
    #Welcome the user
    Welcome()
    #Send the user to the main menu
    Menu()

#Calls the main program if this script is run directly
if __name__ == "__main__":
    main()