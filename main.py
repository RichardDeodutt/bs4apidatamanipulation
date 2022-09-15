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

#Convert country codes to country names
from pycountry import countries

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
def PrintBoredRAWJSON(JSON):
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
    return PrintBoredRAWJSON

#Use subprocess to run a bash script to convert the json to csv
def JSONtoCSV(JSON):
    #Run the bash script and capture the output and return it, bash script takes in a JSON string
    return subprocess.run(['./jsontocsv.sh', json.dumps(JSON)], capture_output=True, text=True).stdout

#Save Bored JSON to CSV file
def SavetoBoredCSV(JSON):
    #Tell the user what we will do
    print('Saving Bored Data to Bored.csv')
    #Convert Bored JSON to CSV
    CSVData = JSONtoCSV(JSON)
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

#Print the formatted and trimmed random activity data
def PrettyPrintBoredJSON(JSON):
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
    return PrettyPrintBoredJSON

#Use subprocess to run a bash script to use the bored api
def GetBored():
    #Run the bash script and capture the output and return it
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
    PrettyPrintBoredJSON(ActivityJSON)
    #Options on what to do with this data
    Options = { "Pretty Print Bored Data": PrettyPrintBoredJSON, "Print All Bored Data": PrintBoredRAWJSON, "Print Raw JSON Bored Data": PrintRAWJSON, 'Save to Bored.csv': SavetoBoredCSV, "Go Back": None }
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

#Get most likely gender from a first name using genderize api
def GetGender(Firstname):
    #Run the bash script and capture the output and return it
    return subprocess.run(['./getgender.sh', Firstname], capture_output=True, text=True).stdout

#Get most likely age from a first name using agify api
def GetAge(Firstname):
    #Run the bash script and capture the output and return it
    return subprocess.run(['./getage.sh', Firstname], capture_output=True, text=True).stdout

#Get most likely nationalitys from a first name using nationalize api
def GetNationalitys(Firstname):
    #Run the bash script and capture the output and return it
    return subprocess.run(['./getnationality.sh', Firstname], capture_output=True, text=True).stdout

#Concatenate the data on first names into one JSON string
def ConcatenateNameData(Gender, Age, Nationalitys):
    #Dictionary containing the final result
    ConcatenatedNameData = {}
    #Changing the name so it won't conflict when merged
    Gender = Gender.replace("probability","gender-probability")
    #Changing the name so it won't conflict when merged and is more descriptive
    Gender = Gender.replace("count","gender-sample-count")
    #Changing the name so it won't conflict when merged and is more descriptive
    Age = Age.replace("count","age-sample-count")
    #Convert from JSON string to Dict
    Gender = json.loads(Gender)
    #Convert from JSON string to Dict
    Age = json.loads(Age)
    #Convert from JSON string to Dict
    Nationalitys = json.loads(Nationalitys)
    #Merge dict to final result dict
    ConcatenatedNameData.update(Gender)
    #Merge dict to final result dict
    ConcatenatedNameData.update(Age)
    #Merge dict to final result dict
    ConcatenatedNameData.update(Nationalitys)
    #return merged final result
    return ConcatenatedNameData

#Pretty Print the formatted and trimmed name data
def PrettyPrintNameJSON(JSON):
    #Print Name
    print('Name:', JSON['name'].capitalize())
    #Print Type
    print('Gender:', JSON['gender'].capitalize())
    #Print Gender-Probability
    print('Gender-Probability:', str(round(JSON["gender-probability"] * 100, 2)) + "%")
    #Print Gender-Sample-Count
    print('Gender-Sample-Count:', JSON['gender-sample-count'])
    #Print Age
    print('Age:', JSON['age'])
    #Print Age-Sample-Count
    print('Age-Sample-Count:', JSON['age-sample-count'])
    #Empty String to store the country probabilities
    CountryString = ""
    #The list of countries
    CountryList = JSON["country"]
    #Go through every country in the list
    for CountryData in CountryList:
        #From the country code get the country
        Country = countries.get(alpha_2=CountryData["country_id"]).name
        #Convert the probability to a percentage
        Probability = round(CountryData["probability"] * 100, 2)
        #Join the two into a string and add it to the CountryString
        if CountryString == "":
            #If the string is empty just add it without a comma
            CountryString += Country + " = " + str(Probability) + "%"
        else:
            #If the string is not empty add it with a comma at the start to seperate it
            CountryString += ", " + Country + " = " + str(Probability) + "%"
    #Print Nationalitys if we found some
    if CountryString != "":
        #Found some so print it
        print('Most Likely Nationalitys and Chances:', CountryString)
    #Return self
    return PrettyPrintBoredJSON

#Analayze a first name
def FirstNameAnalyzer():
    #Ask for user input
    Firstname = input("Enter a first name to analyze (Only letters): ")
    #Don't accept blank input or non letter characters in the input
    if Firstname == "" or not all(Character.isalpha() for Character in Firstname):
        #Name is not valid so tell user
        print("This first name is not valid, can't continue")
    else:
        #Get the predicted gender
        Gender = GetGender(Firstname)
        #Get the predicted age
        Age = GetAge(Firstname)
        #Get the predicted nationalitys
        Nationalitys = GetNationalitys(Firstname)
        #Concatenate the data on first names into one
        ConcatenatedNameDataJSON = ConcatenateNameData(Gender, Age, Nationalitys)
        #Print out the data for the user to see their random activity suggestion
        print('Your Analyzed First Name is as Follows: ')
        #Print out concatenated first name data
        PrettyPrintNameJSON(ConcatenatedNameDataJSON)
        #Options on what to do with this data
        Options = { "Pretty Print Name Data": PrettyPrintNameJSON, "Print All Name Data": None, "Print Raw JSON Name Data": PrintRAWJSON, 'Save to Name.csv': None, "Go Back": None }
        #Infinite Loop
        while True:
            #Space out text for clarity
            print()
            #Bored Menu
            print('Name Menu')
            #Get the user selection
            Selection = Pick('What would you like to do?', Options)
            #User wants to go back
            if Options[Selection] is None:
                #Return back and return self
                return FirstNameAnalyzer
            else:
                #Space out text for clarity
                print()
                #Run the funtion the user selected and pass the JSON data. returning a new function to replace it or with the None type
                Replacement = Options[Selection](ConcatenatedNameDataJSON)
                #Replace the function with what it returned
                Options[Selection] = Replacement

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