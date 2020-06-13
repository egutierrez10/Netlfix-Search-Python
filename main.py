# main.py
#
# Everardo Gutierrez
# Project Netflix Show and Movie LookUp
#   Program will read in file containing movies and shows from Netflix saved to a dataframe. User is then requested on how to
#   search the datafram based on a particular criteria entered.
import pandas as pd 

def printCommands():
    """
        Function: printCommands
        Display all the commands available for the user to enter
        Parameters: 
            none
        Returns:
            none
    """
    print("\nAvailable commands:")
    print("Enter a show or movie name (e.g. The Runner)")
    print("Enter a country (e.g. cUnited States)")
    print("Enter a rating (e.g rPG-13)")
    print("Enter a genre (e.g. gComedies)")
    print("Find movies by year (e.g. 2019)")
    print("Find movies past year, inclusive (e.g. >2019\n")

pd.set_option('display.max_rows', None)
fileName = 'netflix_titles.csv'
print('**Netlfix Movie and TV Show Lookup**')
print('Reading', fileName)
data = pd.read_csv(fileName) # create DataFrame from file entered

choice = input('What you feeling? TV Show or Movie?') # request input from user for what they would like to search for (movie or show)
command = input('Please enter a command, help, or #>') # request command from user for what criteria to search on
while command != "#": # keep searching until user enters # to quit program
    d = data.loc[data.type == choice] # refine dataframe to have only all shows or all movies

    if command == 'help': # user requests to see all commands available to be entered
        printCommands()
    elif command[0] == 'c': # user requests to search based on country
        command = command.replace('c','',1) 
        d = d.loc[d.country.str.contains(command, na = False)] # refine dataframe to contain only shows or movie that have the criteria met
        print(d.title)
    elif command[0] == 'r': # user requests to search based on rating
        command = command.replace('r','',1)
        d = d.loc[d.rating == command]
        print(d.title)
    elif command[0] == 'g': # user requests to search based on genre
        command = command.replace('g','',1)
        d = d.loc[d.listed_in.str.contains(command, na = False)]
        print(d.title)
    elif command.isdigit(): # user requests to search based on year
        d = d.loc[d.release_year == int(command)]
        print(d.title)
    elif command[0] == '>': # user requests to search based on year greater than or equal to the one entered
        command = command.replace('>','',1)
        d = d.loc[d.release_year >= int(command)]
        print(d.title)
    else: # default search based on movie or show title
        d = d.loc[d.title.str.contains(command, na = False)]
        print(d.title)
    
    # request choice and command from user once again
    choice = input('What you feeling? TV Show or Movie?')
    command = input('Please enter a command, help, or #>')  