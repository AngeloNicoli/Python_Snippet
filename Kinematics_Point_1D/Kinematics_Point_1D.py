#############################
# Angelo Nicolì 2024        #
# License: MIT              #
#############################

import time

Point = [None]

print("This script simulate the motion of a particle in a 1D Dimension \n")


def Simulate(Position,Speed,Acceleration,Sim_time):
    for step in range(int(Sim_time)):
        time_step = 1
        print("step" + str(step))
        
        Position = Position + Speed * time_step + 0.5 * Acceleration * pow(time_step,2)
        Speed = Speed + Acceleration * time_step
        print("Position of Point is " + str(Position) + " m. Speed is " + str(Speed) + " m/s. Acceleration is " + str(Acceleration) + " m/s².")
        time.sleep(0.5)
    return Position
  
  
def Validate_Input(input_value):  
    input_value = input_value.replace('.', '')
    if input_value.isnumeric() == True:
        print("Value Inserted is numeric")
        return True
    else:
        ("Please Insert a numeric Value")
        return False


def Ask_input(message):
    input_value = input(message)
    while Validate_Input(input_value) == False
        input_value = input(message)
    return input_value    
    

while True:
    if Point == [None]:   # Create Point
        print("Insert Position of Point.")
        Point[0] = float(input("Plase Insert Coordinate of Point: "))
        print("Point Created. Point is at : " + str(Point[0]) + " m.")
    
    print("Insert, Speed, Acceleration")
    Speed = float(input("insert value of speed (m/s)"))
    Acceleration = float(input ("insert value of acceleration (m²/s)"))
    Sim_time = float(input("insert Time of experiment (s)"))

    Point[0] = Simulate(Point[0],Speed,Acceleration,Sim_time)
    print("New Position is " + str(Point[0]) + "m.")
    if (input("Insert y to continue calculation. Insert any other key to exit")) == "y":
        continue
    else:
        break

