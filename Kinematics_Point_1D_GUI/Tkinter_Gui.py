from tkinter import *
from tkinter import ttk


def Create_Gui():
    m = Tk()
    m.geometry('520x300')
    
    Cord = Label(text = "Cord")
    Cord.grid(row=0, column=0)

    Cord_Input = Entry()
    Cord_Input.grid(row=0, column=2)
    
    Speed = Label(text = "Speed")
    Speed.grid(row= 1, column=0)

    Speed_Input = Entry()
    Speed_Input.grid(row= 1, column=2)

    Acceleration = Label(text = "Acceleration")
    Acceleration.grid(row= 2, column=0)

    Acceleration_Input = Entry()
    Acceleration_Input.grid(row=2, column=2)
    
    Sim_Time = Label(text = "Sim_Time")
    Sim_Time.grid(row= 3, column=0)

    Sim_Time_Input = Entry()
    Sim_Time_Input.grid(row= 3, column=2)

    Calc_Butt = Button(text="Calculate",command= lambda: Set_Parameters(Cord_Input,Speed_Input,Acceleration_Input,Sim_Time_Input))
    Calc_Butt.grid(row=4, column=1)

    mainloop()    


def Set_Parameters(Cord_Input,Speed_Input,Acceleration_Input,Sim_Time_Input):
    print(type(Cord_Input))
    print(Cord_Input.get())

    pass


if __name__ == "__main__":
    Create_Gui()




