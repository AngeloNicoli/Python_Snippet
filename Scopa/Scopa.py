#############################
# Angelo Nicolì 2024        #
# License: MIT              #
#############################

import random
import secrets

Player_Turn = False

Player_Cards = []
Enemy_Cards = []
Board_Card =  []
Player_Cards_Dict ={}

Card_List = list(range(1, 41))


def Identify_Cards():
    for el in Card_List:
        Player_Cards_Dict["Denari"+ str(el)] = str(el)
        print(Player_Cards_Dict)

Card_Deck = Card_List
print(Card_List)

def Card_Identifier():
    for i in range(len(Card_List)):
        pass




def Start_Game():
    # Give Cards to Player

    for i in range(0,3):
        Choosen_Card = secrets.choice(Card_Deck)
        print(Choosen_Card)
        Card_Deck.remove(Choosen_Card)
        Player_Cards.append(Choosen_Card)
        print(Card_Deck)
    # Give Cards to Enemy

    for i in range(0,3):
        Choosen_Card = secrets.choice(Card_Deck)
        print(Choosen_Card)
        Card_Deck.remove(Choosen_Card)
        Enemy_Cards.append(Choosen_Card)
        print(Card_Deck)
    # Display Card to Board
        for i in range(0,3):
            Choosen_Card = secrets.choice(Card_Deck)
            print(Choosen_Card)
            Card_Deck.remove(Choosen_Card)
            Board_Card.append(Choosen_Card)
            print(Card_Deck)


def Turn_Handler():
    print("Tue Carte: " + str(Player_Cards))
    if Player_Turn == False:
        print("Player 1 Turn")
        print("Choose a Card")
    else:
        print("Player 1 Turn")
    


Identify_Cards()
Start_Game()
Turn_Handler()

print(Player_Cards)