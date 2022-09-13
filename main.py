#!/usr/bin/python3

#Richard Deodutt
#09/13/2022
#This script is meant to gather data from a API and organize that data into a csv file using Python and Bash.
#Issues

#Yes or no Prompt
def YNPromt(Prompt):
    #Get the user input
    UserInput=input(Prompt+" Y/N: ")
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

#User is bored so get them a random activity suggestion
def Bored():
    pass

#Main menu of options the user can do
def Menu():
    #Dictionary of options where each entry is a funtion that can be run
    Options = { "I'm Bored": Bored, "Exit": Exit }
    #Infinte Loop
    while True:
        #Get the users selection
        Selection = Pick('What woudld you like to do?', Options)
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