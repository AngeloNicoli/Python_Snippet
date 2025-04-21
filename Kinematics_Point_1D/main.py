#############################
# Angelo Nicolì 2024        #
# License: MIT              #
#############################

import time

Point = [None]

print("This script simulate the motion of a particle in a 1D Dimension \n")

  
def numeric_input_test(input_value):  
    input_value = str(input_value).replace('.', '')
    if input_value.isnumeric() == True:
        print("Value Inserted is numeric")
        return True
    else:
        print("Please Insert a numeric Value")
        return False


def validate_input(input_value):
    while numeric_input_test(input_value) == False:
        input_value = input(input_value)
    return input_value    
    

def Simulate(Position,Speed,Acceleration,Sim_time):
    for step in range(int(Sim_time)):
        time_step = 1
        print("step" + str(step))
        
        Position = Position + Speed * time_step + 0.5 * Acceleration * pow(time_step,2)
        Speed = Speed + Acceleration * time_step
        print("Position of Point is " + str(Position) + " m. Speed is " + str(Speed) + " m/s. Acceleration is " + str(Acceleration) + " m/s².")
        time.sleep(0.5)
    return Position


def get_position():
    print("Insert Position of Point.")
    Point[0] = (input("Plase Insert Coordinate of Point: "))
    Point[0] = float(validate_input(Point[0]))
    print("Point Created. Point is at : " + str(Point[0]) + " m.")
    return Point[0]

def get_parameters():
    print("Insert, Speed, Acceleration")
    Speed = float(input("insert value of speed (m/s)"))
    
    Acceleration = float(input ("insert value of acceleration (m²/s)"))
    Sim_time = float(input("insert Time of experiment (s)"))
    return Speed,Acceleration,Sim_time


def Start_Simulation(Gui_Mode = False):
    if Gui_Mode == False:         # Console Mode
        while True:
            if Point == [None]:   # Create Point
                get_position()
            Speed,Acceleration,Sim_time = get_parameters()
            Point[0] = Simulate(Point[0],Speed,Acceleration,Sim_time)
            print("New Position is " + str(Point[0]) + "m.")
            if (input("Insert y to continue calculation. Insert any other key to exit")) == "y":
                continue
            else:
                break
    else:                      # Gui Mode
        #Get_value()           # Get value from GUI Entry
        Simulate(Point[0],Speed,Acceleration,Sim_time)


if __name__ == "__main__":
    Start_Simulation(Gui_Mode = False)

