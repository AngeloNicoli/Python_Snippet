#############################
# Angelo Nicolì 2024        #
# License: MIT              #
#############################

import random
import secrets
import time
import Update_State
import Tkinter_Gui

Debug_Mode = True

Player_1_Hand = []
Player_2_Hand = []

Board_Card =  []  

Player_Cards_Dict ={}
Board_Cards_Dict = ["Denari"] * 10 + ["Coppe"] * 10 + ["Bastoni"] * 10 + ["Spade"] * 10
Board_Cards_Counter = [0] * 10 + [10] * 10 + [20] * 10 + [30] * 10


Player_Turn = False
Turn_Counter =[0]
Hand_Counter = [0]

Player_1_Points = [0]
Player_2_Points = [0]

Card_List = list(range(1, 41))  # Generate a list of 40 cards
Card_Deck = Card_List           # List of Remaining Coveres Cards of deck (Values Changes during game) 
#print(Card_List)

def debug_print(text_to_print,Debug_Mode):
    if Debug_Mode == True:
        print(text_to_print)


for el in Card_List:
    Player_Cards_Dict[str(el)] = str(el -Board_Cards_Counter[el-1]) + " di " + str(Board_Cards_Dict[el-1])
    #print(Player_Cards_Dict)



def Card_Identifier():
    for i in range(len(Card_List)):
        pass


def Give_Cards():
    # Give Cards to Player
    #print("Card_Deck are" + str(Card_Deck))
    for i in range(0,3):
        Choosen_Card = secrets.choice(Card_Deck)
        #print(Choosen_Card)
        Card_Deck.remove(Choosen_Card)
        Player_1_Hand.append(Choosen_Card)
        #print(Card_Deck)
        print("Player 1 ha pescato la carta: " + str(Choosen_Card))
    # Give Cards to Enemy

    for i in range(0,3):
        Choosen_Card = secrets.choice(Card_Deck)
        #print(Choosen_Card)
        Card_Deck.remove(Choosen_Card)
        Player_2_Hand.append(Choosen_Card)
        #print(Card_Deck)
        print("Player 2 ha pescato la carta: " + str(Choosen_Card))
    # Display Card to Board

    if Hand_Counter[0] == 0:
        for i in range(0,4):
            Choosen_Card = secrets.choice(Card_Deck)
            #print(Choosen_Card)
            Card_Deck.remove(Choosen_Card)
            Board_Card.append(Choosen_Card)
            #print(Card_Deck)
            print("A terra è si trova la carta " + str(Choosen_Card))

    print("Le carte sono state distribuite")                    
    print("Le tue Carte sono: " + str(Player_1_Hand))
    print("Le Carte dell'avversario sono: " + str(Player_2_Hand))
    print("A terra ci sono le seguenti carte" + str(Board_Card))


def Turn(Player_Turn,Hand):
    print("\nHa inizio il round: " + str(Hand))
    input("\n\nInserisci un tasto per continuare ")

    while len(Player_1_Hand) !=0 and len(Player_1_Hand) !=0:
        if Player_Turn == False:
            print("Player 1 Turn")
            #card = input("Choose a Card")
            print("PLayer Cards: " + str(Player_1_Hand))
            card = Player_1_Hand[0]
            #print("Player 1 lancia la carta " + str(card))
            print("Player 1 lancia la carta " + str(Player_Cards_Dict[str(card)]))
            #print(card)
            Board_Card.append(card)
            Player_1_Hand.remove(card)
            #Player_Cards.remove(card)
            Player_Turn = True
            
        if Player_Turn == True:
            print("Player 2 Turn")
            print("PLayer 2 Cards: " + str(Player_2_Hand))
            card = Player_2_Hand[0]
            #print("Player 2 lancia la carta " + str(card))
            print("Player 2 lancia la carta " + str(Player_Cards_Dict[str(card)]))
            Board_Card.append(card)
            Player_2_Hand.remove(card)
            Player_Turn = False  


def Turn_Handler():
    for el in Player_1_Hand:
        print("Tue Carte: " + str(Player_Cards_Dict[str(el)]))
    for el in Player_2_Hand:
        print("Le Carte dell'avversario sono: " + str(Player_Cards_Dict[str(el)]))
    for el in Board_Card:
        print("Le carte sulla plancia di gioco sono: " + str(Player_Cards_Dict[str(el)]))
    #while len(Card_Deck) !=0:

    for i in range(0,5):   # There are 5 rounds in every game
        Turn(Player_Turn,Hand_Counter[0])
        Hand_Counter[0] += 1
        Give_Cards()
        if Card_Deck == []:
            Turn(Player_Turn,Hand_Counter[0])
    
    print("Game finished")
    debug_print(Board_Card,Debug_Mode)
    print(len(Board_Card))    
    print(len(Card_Deck))   
    print(len(Player_1_Hand)) 
    print(len(Player_2_Hand))      
    print(Player_1_Hand)


print("""\nBenvenuto al Gioco della SCOPA (2024).Preparo il campo di gioco...""")

Give_Cards()
Turn_Handler()

Tkinter_Gui.Create_Gui()
