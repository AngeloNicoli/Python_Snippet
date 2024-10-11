from tkinter import *


class tkinter_button:
 def __init__(self,name, Text ="-", Grid =[0,0]):
   self.Name = name
   self.Text = Text
   self.Grid = Grid

Button_List=[]

Button_1 = tkinter_button( name= "Button1", Text ="first", Grid = [1,1])
Button_2 = tkinter_button( name= "Button2", Text ="second", Grid = [1,2])
Button_3 = tkinter_button( name= "Button3", Text ="third", Grid = [0,1])

Button_List.append(Button_1)
Button_List.append(Button_2)
Button_List.append(Button_3)


def Create_Gui():
    m = Tk()
    m.geometry('520x300')
    
    for el in Button_List:
        Calc_Butt = Button(text = el.Text)
        Calc_Butt.grid(row= int(el.Grid[0]), column = el.Grid[1])

    mainloop()    


if __name__ == "__main__":
    Create_Gui()

