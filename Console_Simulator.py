# Functions to ask parameters of functions
import sys

def add():
    c = input("insert First Number")
    d = input("insert Second Number")
    e = int(c) + int(d)
    return e

def subtract():
    c = input("insert First Number")
    d = input("insert Second Number")
    e = int(c) + int(d)
    return e

def multiplicate():
    c = input("insert First Number")
    d = input("insert Second Number")
    e = int(c) + int(d)
    return e

def Help():
    for key in function_dict:
        print(key)
    return "Select a function"

def exit_program():
    sys.exit()
        
# Create a dictionary to store functions
function_dict = {
    'Help': Help,
    'addition': add,
    'subtraction': subtract,
    'Multiplication': multiplicate,
    'Exit' : exit_program
}


print("Type Help for List of functions. Type Exit to esc")

Continue_Calculation = 0

while Continue_Calculation == 0:
    # Check if the selected function exists in the dictionary
    selected_function = input("Enter the name of the function you want to execute: ")
    if selected_function in function_dict:
        # Get the function from the dictionary and execute it
        result = function_dict[selected_function]()
        
        print("Result of", selected_function + ":", result)
    else:
        print("Function not found.")




