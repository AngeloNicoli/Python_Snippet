from colorama import init, Fore, Back, Style

# Inizializza colorama (necessario su Windows)
init(autoreset=True)

# Lista dei colori
colors = [
    Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW,
    Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

color_names = [
    "BLACK", "RED", "GREEN", "YELLOW",
    "BLUE", "MAGENTA", "CYAN", "WHITE"
]

print("8 Colori Normali: \n")
ind_color = 0
print(" ████ " + "0" + "  " + "Black")

for color, name in zip(colors, color_names):
    print(color + " ████ " + str(ind_color) + "  " + name)
    ind_color += 1

print("\n 8 Colori Brillanti (Style.BRIGHT): \n")
for color, name in zip(colors, color_names):
    ind_color += 1
    print(Style.BRIGHT + color + " ████ " + str(ind_color) + "  " + name)