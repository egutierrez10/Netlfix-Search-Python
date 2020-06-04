import pandas as pd 

def printCommands():
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
data = pd.read_csv(fileName)

choice = input('What you feeling? TV Show or Movie?')
command = input('Please enter a command, help, or #>')
while command != "#":
    d = data.loc[data.type == choice]

    if command == 'help':
        printCommands()
    elif command[0] == 'c':
        command = command.replace('c','',1)
        d = d.loc[d.country.str.contains(command, na = False)]
        print(d.title)
    elif command[0] == 'r':
        command = command.replace('r','',1)
        d = d.loc[d.rating == command]
        print(d.title)
    elif command[0] == 'g':
        command = command.replace('g','',1)
        d = d.loc[d.listed_in.str.contains(command, na = False)]
        print(d.title)
    elif command.isdigit():
        d = d.loc[d.release_year == int(command)]
        print(d.title)
    elif command[0] == '>':
        command = command.replace('>','',1)
        d = d.loc[d.release_year >= int(command)]
        print(d.title)
    else:
        d = d.loc[d.title.str.contains(command, na = False)]
        print(d.title)
        
    choice = input('What you feeling? TV Show or Movie?')
    command = input('Please enter a command, help, or #>')  