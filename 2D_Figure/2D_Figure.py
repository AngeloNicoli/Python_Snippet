# Angelo Nicolì

import sys


# This Class store all data about 2D Entity
class Figure_2D:
 def __init__(self,name, Primitive ="0", Points = [0], Edge = [0], Faces = [0], Translation = [0,0], Scale = 1, Rotation = 0):
   self.name = name
   self.Primitive  = Primitive 
   self.Points = Points
   self.Edge = Edge
   self.Faces = Faces
   self.Translation = Translation
   self.Scale = Scale
   self.Rotation = Rotation


Scene_object = {}

P1 = Figure_2D("Body_01")

print(P1.Primitive)


def Add_Asset():
  pass

def command_list():
    for key in operations:
        print(key)
    return "Select a function"

def exit_program():
    sys.exit()

def add_triangle(l=1):
   pass
   
def add_rectangle(l1 =1,l2 = 1):
   global Scene_object
   print("Rectangle Created. " + str(l1) + str(l2))
   Scene_object = {"rectangle": Figure_2D("Body_01"), "brand": "Ford"}
   pass

   
def object_instanced():
   print(Scene_object)


# Store the functions in a dictionary
operations = {
    "add": Add_Asset,
    "help": command_list,
    "exit": exit_program,
    "triangle": add_triangle,
    "rectangle": add_rectangle,
    "object": object_instanced
}

Continue_Calculation = 0

def execute_operation(operation_name, *args, **kwargs):
    operations[operation_name](*args, **kwargs)


def check_function(selected_function):
    # Remove the parentheses
    a = selected_function.replace('(', ',').replace(')', '')
    # Split the string by commas
    parts = a.split(',')
    print(parts)
    if parts[0] in operations:
        print("Execute Command" + str(parts[0]))
        execute_operation(*parts)
    else:
        print("Function not found.")
    return parts


while True:
    selected_function = input("Enter the name of the function you want to execute: ")
    check_function(selected_function)