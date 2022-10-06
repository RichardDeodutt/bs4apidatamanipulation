#!/usr/bin/python3

#Richard Deodutt
#09/13/2022
#This script is meant to gather data from a API and organize that data into a csv file using Python and Bash. This is the CLI.
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
def Welcome(*args):
    #Welcome message, API Data Manipulation
    print("Welcome to ADM - API Data Manipulation")
    return None

#Exits the program
def Exit(*args):
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
    return subprocess.run(['./scripts/jsontocsv.sh', json.dumps(JSON)], capture_output=True, text=True).stdout

#Format the bored data to be more pretty
def PrettyBored(OriginalJSON):
    #Make a Copy of the JSON so we don't edit the original
    JSONData = OriginalJSON.copy()
    #Capitilize Activity
    JSONData['Activity'] = JSONData.pop('activity')
    #Capitilize value
    JSONData["Activity"] = JSONData["Activity"].capitalize()+'.'
    #Capitilize Type
    JSONData['Type'] = JSONData.pop('type')
    #Capitilize value
    JSONData["Type"] = JSONData["Type"].capitalize()
    #Capitilize Participants
    JSONData['Participants'] = JSONData.pop('participants')
    #Capitilize Price
    JSONData['Price-Rating'] = JSONData.pop('price')
    #Convert to a rating out of 10, where higher is more costly
    JSONData['Price-Rating'] = str(round(JSONData['Price-Rating'] * 10, 1))+'/10'
    #Capitilize Accessibility and change it to Inaccessibility as it makes more sense
    JSONData['Inaccessibility-Rating'] = JSONData.pop('accessibility')
    #Convert to a rating out of 10, where higher is more inaccessibility
    JSONData['Inaccessibility-Rating'] = str(round(JSONData['Inaccessibility-Rating'] * 10, 1))+'/10'
    #Capitilize Link
    JSONData['Link'] = JSONData.pop('link')
    #Capitilize Key
    JSONData['Key'] = JSONData.pop('key')
    return JSONData

#Print the formatted and trimmed random activity data
def PrettyPrintBoredJSON(OriginalJSON):
    #Convert Name to a pretty version
    JSONData = PrettyBored(OriginalJSON)
    #Print Activity
    print('Activity:', JSONData['Activity'])
    #Print Type
    print('Type:', JSONData['Type'])
    #Print Participants
    print('Participants:', JSONData['Participants'])
    #Print Price-Rating
    print('Price-Rating:', JSONData['Price-Rating'])
    #Print Inaccessibility-Rating
    print('Inaccessibility-Rating:', JSONData['Inaccessibility-Rating'])
    #Print Link if it's not blank
    if JSONData['Link'] != "":
        print('Link:', JSONData['Link'])
    #Return self
    return PrettyPrintBoredJSON

#Tell the user Bored JSON was saved to CSV file
def AlreadySavedData(OriginalJSON):
    #Tell the user the bored data was already saved to csv
    print('Already saved data')
    #Return self
    return AlreadySavedData

#Save Bored JSON to CSV file
def SavetoBoredCSV(OriginalJSON):
    #Tell the user what we will do
    print('Saving Bored Data to Bored.csv')
    #Convert Bored to a pretty version
    JSONData = PrettyBored(OriginalJSON)
    #Convert Bored JSON to CSV
    CSVData = JSONtoCSV(JSONData)
    #If the file does not exist write to file with the headers
    if not exists('Bored.csv'):
        #Append to the Bored.csv file
        with open('Bored.csv', 'a') as File:
            #Print the data being written
            print(CSVData, end ="")
            #Write with the headers to the file
            File.write(CSVData)
    else:
        #File already exists append to Bored.csv file only the data no header
        with open('Bored.csv', 'a') as File:
            #Print only the data being written no header
            print(CSVData.splitlines()[1])
            #Write the data only no headers to file
            File.write(CSVData.splitlines()[1]+'\n')
    #Save completed
    print('Saved Bored Data to Bored.csv')
    #Return another function so this can't be called for the same data
    #This is not the best or foolproof method to stop duplicate data but it's better than nothing
    return AlreadySavedData

#Use subprocess to run a bash script to use the bored api
def GetBored(*args):
    #Run the bash script and capture the output and return it
    return subprocess.run(['./scripts/getapires.sh', '-b'], capture_output=True, text=True).stdout

#User is bored so get them a random activity suggestion
def Bored(*args):
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
    Options = { "Pretty Print Bored Data": PrettyPrintBoredJSON, "Print All Bored Data": PrintBoredRAWJSON, "Print Raw JSON Bored Data": PrintRAWJSON, 'Save to Bored.csv': SavetoBoredCSV, "Go Back": None, "Exit": Exit }
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
            #Run the funtion the user selected and pass the JSON data. returning a new function to replace it or with the None type, Replace the function with what it returned
            Options[Selection] = Options[Selection](ActivityJSON)

#Get most likely gender from a first name using genderize api
def GetGender(Firstname):
    #Run the bash script and capture the output and return it
    return subprocess.run(['./scripts/getapires.sh', '-g', Firstname], capture_output=True, text=True).stdout

#Get most likely age from a first name using agify api
def GetAge(Firstname):
    #Run the bash script and capture the output and return it
    return subprocess.run(['./scripts/getapires.sh', '-a', Firstname], capture_output=True, text=True).stdout

#Get most likely Nationalities from a first name using nationalize api
def GetNationalities(Firstname):
    #Run the bash script and capture the output and return it
    return subprocess.run(['./scripts/getapires.sh', '-n', Firstname], capture_output=True, text=True).stdout

#Concatenate the data on first names into one JSON string
def ConcatenateNameData(Gender, Age, Nationalities):
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
    Nationalities = json.loads(Nationalities)
    #Merge dict to final result dict
    ConcatenatedNameData.update(Gender)
    #Merge dict to final result dict
    ConcatenatedNameData.update(Age)
    #Merge dict to final result dict
    ConcatenatedNameData.update(Nationalities)
    #return merged final result
    return ConcatenatedNameData

#Format the name data to be more pretty
def PrettyName(OriginalJSON):
    #Make a Copy of the JSON so we don't edit the original
    JSONData = OriginalJSON.copy()
    #Capitilize name
    JSONData['Name'] = JSONData.pop('name')
    #Capitilize value
    JSONData["Name"] = JSONData["Name"].capitalize()
    #Capitilize Gender
    JSONData['Gender'] = JSONData.pop('gender')
    #Capitilize value
    if JSONData["Gender"] is not None:
        JSONData["Gender"] = JSONData["Gender"].capitalize()
    else:
        JSONData["Gender"] = "Unknown"
    #Capitilize Gender-Probability
    JSONData['Gender-Probability'] = JSONData.pop('gender-probability')
    #Convert probability to percent
    JSONData['Gender-Probability'] = str(round(JSONData["Gender-Probability"] * 100, 2)) + "%"
    #Capitilize Gender-Sample-Count
    JSONData['Gender-Sample-Count'] = JSONData.pop('gender-sample-count')
    #Capitilize Age
    JSONData['Age'] = JSONData.pop('age')
    #Print Age-Sample-Count
    JSONData['Age-Sample-Count'] = JSONData.pop('age-sample-count')
    #Empty String to store the country probabilities
    CountryString = ""
    #The list of countries
    CountryList = JSONData["country"]
    #Go through every country in the list
    for CountryData in CountryList:
        #From the country code get the country
        Country = countries.get(alpha_2=CountryData["country_id"]).name
        #Convert the probability to a percentage
        Probability = round(CountryData["probability"] * 100, 2)
        #Join the two into a string and add it to the CountryString
        if CountryString == "":
            #If the string is empty just add it without a dash
            CountryString += Country + " = " + str(Probability) + "%"
        else:
            #If the string is not empty add it with a dash at the start to seperate it
            CountryString += " - " + Country + " = " + str(Probability) + "%"
    #Change country to Most Likely Nationalities and Chances
    JSONData['Most Likely Nationalities and Probabilities'] = JSONData.pop('country')
    JSONData['Most Likely Nationalities and Probabilities'] = CountryString
    return JSONData

#Save Name JSON to CSV file
def SavetoNameCSV(OriginalJSON):
    #Tell the user what we will do
    print('Saving Name Data to Name.csv')
    #Convert Name to a pretty version
    JSONData = PrettyName(OriginalJSON)
    #Convert Name JSON to CSV
    CSVData = JSONtoCSV(JSONData)
    #If the file does not exist write to file with the headers
    if not exists('Name.csv'):
        #Append to the bored.csv file
        with open('Name.csv', 'a') as File:
            #Print the data being written
            print(CSVData, end ="")
            #Write with the headers to the file
            File.write(CSVData)
    else:
        #File already exists append to bored.csv file only the data no header
        with open('Name.csv', 'a') as File:
            #Print only the data being written no header
            print(CSVData.splitlines()[1])
            #Write the data only no headers to file
            File.write(CSVData.splitlines()[1]+'\n')
    #Save completed
    print('Saved Name Data to Name.csv')
    #Return another function so this can't be called for the same data
    #This is not the best or foolproof method to stop duplicate data but it's better than nothing
    return AlreadySavedData

#Pretty Print the formatted and trimmed name data
def PrettyPrintNameJSON(OriginalJSON):
    #Convert Name to a pretty version
    JSONData = PrettyName(OriginalJSON)
    #Print Name
    print('Name:', JSONData['Name'])
    #Print Gender
    print('Gender:', JSONData['Gender'])
    #Print Gender-Probability
    print('Gender-Probability:', JSONData['Gender-Probability'])
    #Print Gender-Sample-Count
    print('Gender-Sample-Count:', JSONData['Gender-Sample-Count'])
    #Print Age
    print('Age:', JSONData['Age'])
    #Print Age-Sample-Count
    print('Age-Sample-Count:', JSONData['Age-Sample-Count'])
    #Print Nationalities if we found some
    if JSONData['Most Likely Nationalities and Probabilities'] != "":
        #Found some so print it
        print('Most Likely Nationalities and Chances:', JSONData['Most Likely Nationalities and Probabilities'])
    #Return self
    return PrettyPrintNameJSON

#Get all the first name data from the api and concatenate it
def GetName(Firstname):
    #Get the predicted gender
    Gender = GetGender(Firstname)
    #Get the predicted age
    Age = GetAge(Firstname)
    #Get the predicted nationalities
    Nationalities = GetNationalities(Firstname)
    #Concatenate the data on first name into one
    ConcatenatedNameDataJSON = ConcatenateNameData(Gender, Age, Nationalities)
    #Return the concatenated data
    return ConcatenatedNameDataJSON

#Analayze a first name
def FirstNameAnalyzer(*args):
    #Ask for user input
    Firstname = input("Enter a first name to analyze (Only letters): ")
    #Don't accept blank input or non letter characters in the input
    if Firstname == "" or not all(Character.isalpha() for Character in Firstname):
        #Name is not valid so tell user
        print("This first name is not valid, can't continue")
    else:
        #Concatenate the data on first name into one
        ConcatenatedNameDataJSON = GetName(Firstname)
        #Print out the data for the user to see their random activity suggestion
        print('Your Analyzed First Name is as Follows: ')
        #Print out concatenated first name data
        PrettyPrintNameJSON(ConcatenatedNameDataJSON)
        #Options on what to do with this data
        Options = { "Pretty Print Name Data": PrettyPrintNameJSON, "Print All Name Data": PrintBoredRAWJSON, "Print Raw JSON Name Data": PrintRAWJSON, 'Save to Name.csv': SavetoNameCSV, "Go Back": None, "Exit": Exit }
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
                #Run the funtion the user selected and pass the JSON data. returning a new function to replace it or with the None type, Replace the function with what it returned
                Options[Selection] = Options[Selection](ConcatenatedNameDataJSON)

#Main menu of options the user can do
def Menu(*args):
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
        #Run the funtion the user selected. returning a new function to replace it, Replace the function with what it returned
        Options[Selection] = Options[Selection]()

#The main program
def main(*args):
    #Welcome the user
    Welcome()
    #Send the user to the main menu
    Menu()

#Calls the main program if this script is run directly
if __name__ == "__main__":
    main()