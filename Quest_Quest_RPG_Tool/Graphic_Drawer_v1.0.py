from tkinter import *
import math
from tkinter import simpledialog
import Export_png
from tkinter import ttk
import os

# Size of Main Window
window_width = 300
window_height = 100


# Create Main Window
root = Tk()
root.geometry(str(window_width) + "x" + str(window_height))
root.title("Map Drawer")
root.configure(bg='#A2AF9B')

valore_iniziale = StringVar()
valore_iniziale.set("600")

Entry_1 = Entry(root,text = valore_iniziale)
Entry_1.grid(row= 0, column = 1,padx = 20)

Label_1 = Label(root,text = "Grandezza Quadrato (px)")
Label_1.grid(row= 0, column = 0)


Entry_1 = Entry(root,text = valore_iniziale)
Entry_1.grid(row= 1, column = 1,padx = 20)

Label_1 = Label(root,text = "Larghezza Tela px")
Label_1.grid(row= 1, column = 0)


Entry_1 = Entry(root,text = "Lunghezza Tela (px)")
Entry_1.grid(row= 2, column = 1,padx = 20)

Label_1 = Label(root,text = "Lunghezza Tela px")
Label_1.grid(row= 2, column = 0)


def save_input():
    print("£")
    root.destroy()


Button1 = Button(text = "Crea nuovo canvas", bg="#D9E9CF",fg ="#556B2F",command = save_input)
Button1.grid(row= 3, column=0,columnspan = 10,pady=2, padx = 20,sticky = W+E)   


root.mainloop()


window_width = 610
window_height = 730


# Create Main Window
root = Tk()
root.geometry(str(window_width) + "x" + str(window_height))
root.title("Map Drawer")
root.configure(bg='#A2AF9B')

#root.configure(bg="white")

# Size of Canvas
Canvas_width = 600
Canvas_height = 600
Center_Canvas = [Canvas_width/2,Canvas_height/2]

# Define number of row, column and pixel_size

pixel_size = 5

row = int(Canvas_height/pixel_size)
column = int(Canvas_width/pixel_size)


# Create Canvas
canvas = Canvas(width=Canvas_width, height= Canvas_height, bg='gray')  
canvas.grid(row=0, column=0 , columnspan = 8, padx=5)
canvas.configure(bg='black')


def createMatrix(row, col):
    mat = []
    for el in range(row):
        mat.append([0]*col)
    return mat


Color_Grid = createMatrix(int(Canvas_width/pixel_size), int(Canvas_height/pixel_size))


Color_Map = createMatrix(int(Canvas_width/pixel_size), int(Canvas_height/pixel_size))

#print(Color_Grid)

# Load matrix from txt file
def render_image(image_name):
    
    render_matrix = []

    with open("palette\\" + image_name + ".txt", "r") as file:
        i = 0
        for line in file:
            line = line.strip()
            render_matrix.append("#" + line)
            print(render_matrix[i])
            i +=1

    return render_matrix
  
  
Background_color =[[None],[None]]
Background_color[0] = render_image("win_palette_1")  
Background_color[1] = render_image("win_palette_2")  
print(Background_color)


#Background_color = [["Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White"],["Gray", "Indian red", "limegreen", "khaki1", "skyblue2", "purple", "darkslategray3", "azure1"]]
#Background_color = [["Black", "#6723ab", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White"],["Gray", "Indian red", "limegreen", "khaki1", "skyblue2", "purple", "darkslategray3", "#06ffff"]]  
Background_hex_color = [[None]*8,[None]*8]

Color_Code = {"Black": 0, "Red":1,"Green":2,"Yellow": 3,"Blue": 4,"Magenta": 5,"Cyan": 6,"White": 7,"Gray": 8, "Indian red": 9, "limegreen": 10,"khaki1": 11,"skyblue2": 12, "purple": 13, "darkslategray3": 14,"azure1": 15 }
Color_Code_hex_color ={}
Color_Label =[None]*8

current_color = [Background_color[0][0]]
print("Colore Selezionato" +str(current_color[0]))

def color_to_hex(color_name):
    r, g, b = root.winfo_rgb(color_name)
    return "#{:02x}{:02x}{:02x}".format(r//256, g//256, b//256)


for i in range(0,2):
    for j in range(0,8):
        Background_hex_color[i][j] = color_to_hex(Background_color[i][j])
    print(i)
 
 
for i in range(0,2):
    for j in range(0,8):
        Color_Code_hex_color[Background_hex_color[i][j]] = (8*i)+j
    
    
 
print(Color_Code_hex_color) 
 
print(Background_color)
print(Background_hex_color)


#Create Label with Color
for i in range(0,2):
    for j in range(0,8):
        Color_Label[j] = Label(root,text="", bg= Background_hex_color[i][j], borderwidth=1,relief="solid",padx=20)
        Color_Label[j].grid(row= i+1, column=j,pady=2)   
        Color_Label[j].bind("<Button-1>", lambda e, c=Background_hex_color[i][j]:printatore(c))
        #print(Color_Label[j].cget("bg"))
 
def Scrivi_Mappa():
    #print(Color_Grid)
    name_file = simpledialog.askstring("Input", "Esporta il tuo file per 'Quest Quest'")
    open(str(name_file) + '.txt', 'w').close()
    for el in range(len(Color_Grid)):
        with open(str(name_file) + '.txt', 'a') as f:
            f.write(", ".join(str(x) for x in Color_Grid[el])+ "\n")


def Esporta_png():
    # Inverti chiavi e valori
    Color_Palette = {v: k for k, v in Color_Code_hex_color.items()}
    print(Color_Palette)
    for el in range(len(Color_Grid)):
         for ely in range(len(Color_Grid[el])):
            Color_Map[el][ely] = Color_Palette[Color_Grid[ely][el]]
    print(Color_Map)

    name_file = simpledialog.askstring("Input", "Esporta il tuo file in formato png'")
    Export_png.esporta(Canvas_width,Canvas_height,pixel_size,Color_Map)


#Button1 = ttk.Button(text = "Scrivi_Mappa", command = Scrivi_Mappa)
#Button1.grid(row= 4, column=0,columnspan = 10,pady=2, sticky = W+E)   

Button1 = Button(text = "Scrivi_Mappa", bg="#D9E9CF",fg ="#556B2F",command = Scrivi_Mappa)
Button1.grid(row= 4, column=0,columnspan = 10,pady=2, padx = 20,sticky = W+E)   

Button2 = Button(text = "Esporta png", bg="#D9E9CF",fg ="#556B2F",command = Esporta_png)
Button2.grid(row= 5, column=0,columnspan = 10,pady=2, padx = 20,sticky = W+E)   


def printatore(color_print):
    #print(color_print)
    current_color[0] = color_print
    return current_color


#Red_Color = Label(root,text="", bg="#c50f1f", borderwidth=1,relief="solid")
#Red_Color.grid(row=1, column=1,sticky=W+E, padx=5, ipadx=10)



def Save_Matrix():
    print("save")


def draw_pixel(row,column,color,pixel_size,cordx,cordy,color_index):
      #print(row,column,color)
      #cordy = (row) * pixel_size
      #cordx = (column) * pixel_size
      #print(cordx)
      #print(cordy)
      cordx = math.floor(cordx/pixel_size) * pixel_size
      cordy = math.floor(cordy/pixel_size) * pixel_size
      #print(cordx)
      #print(cordy)
      #print("color index is" + str(color_index))
      Color_Grid[math.floor(cordy/pixel_size)][math.floor(cordx/pixel_size)] = color_index
      
      #print(Color_Grid)
      #print("\n")
      #print(Color_Grid[1])
      #print("\n")
      #print(Color_Grid[2])
      #print(str(row) + " " + str(column))
      if color == '0':
        color = "white"
      canvas.create_rectangle(cordx, cordy, cordx + pixel_size, cordy + pixel_size , width = 0, fill = color , tags="pixel")
      #canvas.create_rectangle(0, 0, 30,30, width = 0, fill = color , tags="pixel")
      #pixel_color[row][column] = color
      
      #open('demofile.txt', 'w').close()
      #for el in range(len(Color_Grid)):
        #with open("demofile.txt", "a") as f:
            #f.write(", ".join(str(x) for x in Color_Grid[el])+ "\n")
            #f.write(str(Color_Grid[el])+"\n")  

def mostra_coordinate(event):
    # event.x e event.y contengono le coordinate relative al Canvas
    #print(Color_Code[str(current_color[0])])
    draw_pixel(row,column,current_color[0],pixel_size,event.x,event.y, Color_Code_hex_color[str(current_color[0])]) #row,column, 
    print(f"Click a: x={event.x}, y={event.y}")
    
    
# Collega il click del mouse (tasto sinistro) alla funzione
canvas.bind("<Button-1>", mostra_coordinate)
canvas.bind("<B1-Motion>", mostra_coordinate)

root.mainloop()



