from tkinter import *
from tkinter import ttk

def Create_Gui():
    m = Tk()
    m.geometry('520x300')
    
    Player_1_Card_1 = Label(text = "Player 1 Card 1")
    Player_1_Card_1.grid(row=0, column=0)
    Player_1_Card_2 = Label(text = "Player 1 Card 2")
    Player_1_Card_2.grid(row=0, column=1)
    Player_1_Card_3 = Label(text = "Player 1 Card 3")
    Player_1_Card_3.grid(row=0, column=2)

    Board_Card = Label(text="\n Board Card: 1,2,3,4 \n")
    Board_Card.grid(row=2, column=1)

    Player_2_Card_1 = Label(text = "Player 2 Card 1")
    Player_2_Card_1.grid(row=3, column=0)
    Player_2_Card_2 = Label(text = "Player 2 Card 2")
    Player_2_Card_2.grid(row=3, column=1)
    Player_2_Card_3 = Label(text = "Player 2 Card 3")
    Player_2_Card_3.grid(row=3, column=2)

    image = PhotoImage(file="1_Denari.png")
    label = ttk.Label(image=image)
    label.grid(row=4, column=0)


    mainloop()    


if __name__ == "__main__":
    Create_Gui()




