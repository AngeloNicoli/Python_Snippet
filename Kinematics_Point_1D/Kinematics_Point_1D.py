#############################
# Angelo Nicolì 2024        #
# License: MIT              #
#############################

import time

Point = [None]

def Simulate(Position,Speed,Acceleration,Sim_time):
    for step in range(int(Sim_time)):
        time_step = 1
        print("step" + str(step))
        
        Position = Position + Speed * time_step + 0.5 * Acceleration * pow(time_step,2)
        Speed = Speed + Acceleration * time_step
        print("Position of Point is " + str(Position) + " m. Speed is " + str(Speed) + " m/s. Acceleration is " + str(Acceleration) + " m/s².")
        time.sleep(0.5)
    pass


while True:
    if Point == [None]:   # Create Point
        print("Insert Position of Point.")
        Point[0] = float(input("Plase Insert Coordinate of Point: "))
        print("Point Created. Point is at : " + str(Point[0]) + " m.")
    
    print("Insert, Speed, Acceleration")
    Speed = float(input("insert value of speed (m/s)"))
    Acceleration = float(input ("insert value of acceleration (m²/s)"))
    Sim_time = float(input("insert Time of experiment (s)"))

    Simulate(Point[0],Speed,Acceleration,Sim_time)
     
    



