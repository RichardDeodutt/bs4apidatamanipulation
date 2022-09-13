#!/usr/bin/python3

#Richard Deodutt
#09/13/2022
#This script is meant to gather data from a API and organize that data into a csv file using Python and Bash.
#Issues

#Subprocess to run bash scripts
import subprocess

#Neede to convert the api data to usable format
import json

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

def SavetoBored(JSON):
    pass

#User is bored so get them a random activity suggestion
def Bored():
    #Tell the user what we will do
    print('Let me suggest a random activity you can do then!')
    #Subprocess call to the bash script to get a random activity suggestion using a api and curl
    ActivityData = subprocess.run(['./bored.sh'], capture_output=True, text=True).stdout
    #Convert the string into a dictionary using json
    ActivityJSON = json.loads(ActivityData)
    #Print out the data for the user to see their random activity suggestion
    print('Your Random Activity is as Follows: ')
    #Print Activity
    print('Activity:', ActivityJSON['activity'].capitalize()+'.')
    #Print Type
    print('Type:', ActivityJSON['type'].capitalize())
    #Print Participants
    print('Participants:', ActivityJSON['participants'])
    #Print Price
    print('Price:', str(round(ActivityJSON['price'] * 10, 1))+'/10')
    #Print Accessibility
    print('Accessibility:', str(round(ActivityJSON['accessibility'] * 10, 1))+'/10')
    #Print Link if it's not blank
    if ActivityJSON['link'] != "":
        print('Link:', ActivityJSON['link'])
    #Options on what to do with this data
    Options = { "Print Data": PrintJSON, "Print Raw Data": PrintRAWJSON, 'Save to Bored.csv': SavetoBored, "Go Back": None }
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
            #Return back
            return None
        else:
            #Space out text for clarity
            print()
            #Run the funtion the user selected and pass the JSON data
            Options[Selection](ActivityJSON)

#Main menu of options the user can do
def Menu():
    #Dictionary of options where each entry is a funtion that can be run
    Options = { "I'm Bored": Bored, "Exit": Exit }
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
        #Run the funtion the user selected
        Options[Selection]()

#The main program
def main():
    #Welcome the user
    Welcome()
    #Send the user to the main menu
    Menu()

#Calls the main program
main()