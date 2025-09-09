######################################
'''
Autore:
    Angelo Nicolì "Gengio"

Data:
    08 settembre 2025

'''
######################################


from colorama import init, Fore, Back, Style
import os # clear the console screen
import sys 
import random
import terrain
import Table_Formatter


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
    self.defence = 10
    self.exp = 0
    self.speed = 0
    self.bio = "E' nato"
    self.stats = [self.Level,self.attack,self.defence,self.exp,self.speed]
    self.equipment = {}
    self.inventory = {}
    
    
#inventory = {"Coin":"20 Monete", "Mantello":"Mantello di pelle", "Oggetto": "Otre Pieno d'acqua"}    
#print(Player_1.health) 
    
Player_1 = Player()  
 
terrain_map = terrain.terrain_generator()
sword_icon = terrain.sword_generator()


#for i in range(0,10):
    #print(color_fore[0] + "4", end='')
    #print(color_fore[1] + "4")

def start_quest(): 
    for i in range (0,1):
        print("\n")
    narrator_text = Fore.MAGENTA + Back.WHITE 
    print(Fore.MAGENTA + Back.WHITE + "Benvenuto su Quest Quest." + Style.RESET_ALL + Fore.MAGENTA + "\n \nInserisci <start> per iniziare l'avventura" + Style.RESET_ALL)

    for i in range (0,1):
        print("\n")

    start_quest = input("Scegli il tuo destino ")
    
    if start_quest == "start":
        print("Molto bene. Eccoti dell'equipaggiamento per iniziare l'avventura)\n")
        print("Hai ricevuto 50 monete d'oro.- \n Hai ricevuto un mantello di pelle ")
        obtain_object("Coin","50 Monete")
        obtain_object("Mantello","Mantello di Pelle")
    else:
        print("Non vuoi giocare. peccato")
        sys.exit()

def obtain_object(key_obj,conten_inv):
    Player_1.inventory[key_obj] = conten_inv
    print(Player_1.inventory)


def player_turn():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + "Scegli la tua prossima azione:" + Style.RESET_ALL + "\n 1 - Controlla la mappa.  \n 2- Controlla inventario \n 3- Controlla statistiche\n 4 - Controlla Equipaggiamento\n 5 - Vai verso città più vicina \n 6 - Vai verso dungeon più vicino\n 7 - Esci dal gioco")
    player_choice = input()
    if player_choice == "1":  # Map show
        map_show()
    if player_choice == "2":  # Show inventory
        inventory_show()
    if player_choice == "3":  # Show Status
        status_show()
    if player_choice == "4":  # Show Equipment
        equipment_show()   
    if player_choice == "5":  # Move Settlement
        move_settlement()
    if player_choice == "6":  # Move Dungeon
        move_dungeon()   
    if player_choice == "7":  # Exit Game
        sys.exit()   
   
    input("\n Inserisci un tasto qualsiasi per continuare")
    player_turn()
    pass


def map_show():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0,20):
        for j in range (0,20):
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
    print("Ti fermi un attimo perché non ti ricordi cosa hai nello zaino. Meglio dare un'occhiata...")
    for el in Player_1.inventory:
        print(str(Player_1.inventory[el]))
    print("\n")
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "Mostra status\n Guardi dentro te stesso. Ecco cosa vedi: " + Style.RESET_ALL)
    print(Player_1.name)
       
    '''self.name = name
    self.age = age
    self.Level = 1
    self.health = 100
    self.attack = 10 
    self.equipment = {}
    self.inventory = {}'''

def equipment_show():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "Mostra equipaggiamento\n Chissà cosa indosso. Meglio girare la testa verso il basso" + Style.RESET_ALL)


def move_settlement():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "Hai scelto. Muovi verso insediamento\n Mi dirigerò verso la città piu' vicina" + Style.RESET_ALL)
    print("Life = 100 Hp")
    
def move_dungeon():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "Hai scelto. Muovi verso dungeon\n Sono pronto alla battaglia. Verso la prossima avventura!!" + Style.RESET_ALL)
    print("Life = 100 Hp") 



 
# Initialize Game
start_quest()


# Start Player Turn
player_turn()







