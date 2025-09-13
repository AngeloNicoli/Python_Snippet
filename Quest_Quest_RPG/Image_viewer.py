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


def render_image(image_map):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0,20):
        for j in range (0,20):
            pixel_color = color_fore[image_map[i][j]]
            #pixel_color = color_fore[random.randint(1,7)]
            print(pixel_color+ "█"+ Style.RESET_ALL, end="")
            print(pixel_color+ "█"+ Style.RESET_ALL, end="")

        #pixel_color = color_fore[random.randint(1,7)]
        pixel_color = color_fore[image_map[i][j]]
        print(pixel_color +"█"+ Style.RESET_ALL, end="")
        print(pixel_color +"█"+ Style.RESET_ALL)
    
    
name_file = input("inserisci nome del file")

image_map = terrain.render_image(str(name_file))
render_image(image_map)

input("Premi un tasto per continuare")