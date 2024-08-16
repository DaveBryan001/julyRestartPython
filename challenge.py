import json

# Define the file path
file = 'names.json'

# Initialize the name variable
name = ""

# Try to open the file and load the name from it
try:
    open(file, "r")  # Open the file for reading
    name = json.load(open(file, "r"))  # Load the name from the file
except IOError:
    print("User doesn't exist")

# Check if the name is not empty
if name != "":
    print("Hello " + name)
else:
    name = input("What is your name? ")  # Prompt the user for their name
    print("Hello " + name)
try:
        open(name, 'w')
        # json.dump(name, f)
        json.dump(name, open(file, "w"))  # Save the name to the file
except IOError:
    print("There was a problem writing to the history file.")








