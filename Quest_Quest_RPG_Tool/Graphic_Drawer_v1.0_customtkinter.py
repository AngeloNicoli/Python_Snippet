import customtkinter as ctk
import math
from tkinter import simpledialog
import Export_png
import os

try:
    # For Windows: forza DPI awareness
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(2)  # 1 = System DPI, 2 = Per-monitor DPI
    print("X")
except:
    pass

# ======================
# CONFIGURAZIONE CUSTOMTKINTER
# ======================
ctk.set_appearance_mode("system")   # "dark", "light", "system"
ctk.set_default_color_theme("green")

# ======================
# PRIMA FINESTRA (INPUT)
# ======================
window_width = 350
window_height = 200

root = ctk.CTk()
root.geometry(f"{window_width}x{window_height}")
root.title("Map Drawer")

valore_iniziale = ctk.StringVar(value="600")

# Entry e Label
label1 = ctk.CTkLabel(root, text="Grandezza Quadrato (px)")
label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1 = ctk.CTkEntry(root, textvariable=valore_iniziale)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = ctk.CTkLabel(root, text="Larghezza Tela px")
label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = ctk.CTkEntry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

label3 = ctk.CTkLabel(root, text="Lunghezza Tela px")
label3.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry3 = ctk.CTkEntry(root)
entry3.grid(row=2, column=1, padx=10, pady=5)

def save_input():
    print("£")
    root.destroy()

button1 = ctk.CTkButton(root, text="Crea nuovo canvas", command=save_input)
button1.grid(row=3, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

root.mainloop()


# ======================
# SECONDA FINESTRA (CANVAS)
# ======================

window_width2 = 800
window_height2 = 800

root = ctk.CTk()
root.geometry(f"{window_width2}x{window_height2}")
root.title("Map Drawer")

# Dimensioni canvas
Canvas_width = 600
Canvas_height = 600
#Center_Canvas = [Canvas_width/2, Canvas_height/2]

pixel_size = 20
row = int(Canvas_height/pixel_size)
column = int(Canvas_width/pixel_size)

# Canvas
canvas = ctk.CTkCanvas(root, width=Canvas_width, height=Canvas_height, bg="black", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=8, padx = 75, pady=5)

# ======================
# FUNZIONI DI SUPPORTO
# ======================
def createMatrix(row, col):
    return [[0]*col for _ in range(row)]

Color_Grid = createMatrix(int(Canvas_width/pixel_size), int(Canvas_height/pixel_size))
Color_Map = createMatrix(int(Canvas_width/pixel_size), int(Canvas_height/pixel_size))

def render_image(image_name):
    render_matrix = []
    with open("palette\\" + image_name + ".txt", "r") as file:
        for line in file:
            line = line.strip()
            render_matrix.append("#" + line)
    return render_matrix

Background_color = [[None],[None]]
Background_color[0] = render_image("win_palette_1")
Background_color[1] = render_image("win_palette_2")

Background_hex_color = [[None]*8,[None]*8]

Color_Code = {
    "Black": 0, "Red":1,"Green":2,"Yellow":3,"Blue":4,"Magenta":5,"Cyan":6,"White":7,
    "Gray": 8, "Indian red": 9, "limegreen": 10,"khaki1": 11,"skyblue2": 12,
    "purple": 13, "darkslategray3": 14,"azure1": 15
}
Color_Code_hex_color = {}
Color_Label = [None]*8
current_color = [Background_color[0][0]]

def color_to_hex(color_name):
    r, g, b = root.winfo_rgb(color_name)
    return "#{:02x}{:02x}{:02x}".format(r//256, g//256, b//256)

for i in range(0,2):
    for j in range(0,8):
        Background_hex_color[i][j] = color_to_hex(Background_color[i][j])

for i in range(0,2):
    for j in range(0,8):
        Color_Code_hex_color[Background_hex_color[i][j]] = (8*i)+j

def printatore(color_print):
    current_color[0] = color_print
    return current_color

# Palette colori
for i in range(0,2):
    for j in range(0,8):
        Color_Label[j] = ctk.CTkLabel(root, text="", width=40, height=20,
                                      fg_color=Background_hex_color[i][j],
                                      corner_radius=4)
        Color_Label[j].grid(row=i+1, column=j, pady=2, padx=2)
        Color_Label[j].bind("<Button-1>", lambda e, c=Background_hex_color[i][j]: printatore(c))

# ======================
# FUNZIONI DI EXPORT
# ======================
def Scrivi_Mappa():
    name_file = simpledialog.askstring("Input", "Esporta il tuo file per 'Quest Quest'")
    open(str(name_file) + '.txt', 'w').close()
    for el in range(len(Color_Grid)):
        with open(str(name_file) + '.txt', 'a') as f:
            f.write(", ".join(str(x) for x in Color_Grid[el])+ "\n")

def Esporta_png():
    Color_Palette = {v: k for k, v in Color_Code_hex_color.items()}
    for el in range(len(Color_Grid)):
        for ely in range(len(Color_Grid[el])):
            Color_Map[el][ely] = Color_Palette[Color_Grid[ely][el]]
    name_file = simpledialog.askstring("Input", "Esporta il tuo file in formato png'")
    Export_png.esporta(Canvas_width, Canvas_height, pixel_size, Color_Map)

button2 = ctk.CTkButton(root, text="Scrivi Mappa", command=Scrivi_Mappa)
button2.grid(row=4, column=0, columnspan=8, pady=5, padx=20, sticky="ew")

button3 = ctk.CTkButton(root, text="Esporta PNG", command=Esporta_png)
button3.grid(row=5, column=0, columnspan=8, pady=5, padx=20, sticky="ew")

# ======================
# FUNZIONI DI DISEGNO
# ======================
def draw_pixel(row,column,color,pixel_size,cordx,cordy,color_index):
    cordx = math.floor(cordx/pixel_size) * pixel_size
    cordy = math.floor(cordy/pixel_size) * pixel_size
    Color_Grid[math.floor(cordy/pixel_size)][math.floor(cordx/pixel_size)] = color_index
    if color == '0':
        color = "white"
    canvas.create_rectangle(cordx, cordy, cordx+pixel_size, cordy+pixel_size, width=0, fill=color, tags="pixel")

def mostra_coordinate(event):
    draw_pixel(row, column, current_color[0], pixel_size, event.x, event.y, Color_Code_hex_color[str(current_color[0])])

canvas.bind("<Button-1>", mostra_coordinate)
canvas.bind("<B1-Motion>", mostra_coordinate)

root.mainloop()
