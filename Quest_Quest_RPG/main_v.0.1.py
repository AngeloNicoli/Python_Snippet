from colorama import init, Fore, Back, Style
import os # clear the console screen
import sys 
import random
import terrain

os.system('cls' if os.name == 'nt' else 'clear')

#terrain.terrain_generator()

color_fore = [Fore.BLACK,Fore.RED, Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.CYAN, Fore.WHITE, 
Style.BRIGHT + Fore.BLACK,Style.BRIGHT + Fore.RED,Style.BRIGHT + Fore.GREEN,Style.BRIGHT + Fore.YELLOW,
Style.BRIGHT + Fore.BLUE,Style.BRIGHT + Fore.MAGENTA,Style.BRIGHT + Fore.CYAN,Style.BRIGHT + Fore.WHITE]

color_back = [Back.BLACK,Back.RED, Back.GREEN,Back.YELLOW,Back.BLUE,Back.MAGENTA,Back.CYAN, Back.WHITE]

init()

class Player:
  def __init__(self, name = "Player 1", age = "30"):
    self.name = name
    self.age = age
    self.Level = 1
    self.health = 100
    self.attack = 10 
    
Player_1 = Player()  
print(Player_1.health) 
    
    
terrain_map = terrain.terrain_generator()
sword_icon = terrain.sword_generator()

for i in range (0,2):
    print("\n")

narrator_text = Fore.MAGENTA + Back.WHITE 

print(Fore.MAGENTA + Back.WHITE + "Benvenuto su Quest Quest. \n \nInserisci <start> per iniziare l'avventura" + Style.RESET_ALL)

for i in range (0,2):
    print("\n")

start_quest = input("Scegli il tuo destino ")

inventory = {"Coin":"20 Monete", "Mantello":"Mantello di pelle", "Oggetto": "Otre Pieno d'acqua"}


def obtain_object(key_obj,conten_inv):
    inventory[key_obj] = conten_inv
    print(inventory)


if start_quest == "start":
    print("Molto bene. Eccoti dell'equipaggiamento per iniziare l'avventura) \n Hai ricevuto 20 monete d'oro.- \n Hai ricevuto un mantello di pelle ")
    obtain_object("Coin",50)
else:
    print("Non vuoi giocare. peccato")
    sys.exit()


def player_turn():
    print("\n")
    print(Fore.MAGENTA + "Scegli la tua prossima azione:" + Style.RESET_ALL + "\n 1 - Controlla la mappa.  \n 2- Controlla inventario \n 3- Controlla statistiche\n 4 - Controlla Equipaggiamento\n 5 - Vai verso città più vicina \n 6 - Vai verso dungeon più vicino\n 7 - Esci dal gioco")
    player_choice = input()
    if player_choice == "1":
        map_show()
    if player_choice == "2":
        inventory_show()
    if player_choice == "3":
        status_show()
    if player_choice == "7":
        sys.exit()
    player_turn()
    pass

def map_show():
    for i in range(0,20):
        for j in range (0,21):
            pixel_color = color_fore[terrain_map[i][j]]
            #pixel_color = color_fore[random.randint(1,7)]
            print(pixel_color+ "█"+ Style.RESET_ALL, end="")
            print(pixel_color+ "█"+ Style.RESET_ALL, end="")

        #pixel_color = color_fore[random.randint(1,7)]
        pixel_color = color_fore[terrain_map[i][j]]
        print(pixel_color +"█"+ Style.RESET_ALL, end="")
        print(pixel_color +"█"+ Style.RESET_ALL)
    print(Fore.RED + " █ Posizione del Giocatore" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.BLACK + " █ Insediamento piu' vicino: Torre Assolata" + Style.RESET_ALL)


def inventory_show():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Ti fermi un attimo perché non ti ricordi cosa hai nello zaino. Meglio dare un'occhiata... \n \n \n")
    for el in inventory:
        print(str(inventory[el]))
    print("\n \n \n")
    for i in range(0,20):
        for j in range (0,21):
            pixel_color = color_fore[sword_icon[i][j]]
            #pixel_color = color_fore[random.randint(1,7)]
            print(pixel_color+ "█"+ Style.RESET_ALL, end="")
            print(pixel_color+ "█"+ Style.RESET_ALL, end="")

        #pixel_color = color_fore[random.randint(1,7)]
        pixel_color = color_fore[sword_icon[i][j]]
        print(pixel_color +"█"+ Style.RESET_ALL, end="")
        print(pixel_color +"█"+ Style.RESET_ALL)
     
 
def status_show():
    print("Life = 100 Hp")

player_turn()

for i in range(0,10):
    print(color_fore[0] + "4", end='')
    print(color_fore[1] + "4")








