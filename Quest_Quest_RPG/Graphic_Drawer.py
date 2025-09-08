from tkinter import *
import math

# Size of Main Window
window_width = 610
window_height = 700

# Create Main Window
root = Tk()
root.geometry(str(window_width) + "x" + str(window_height))
root.title("Map Drawer")

#root.configure(bg="white")

# Size of Canvas
Canvas_width = 600
Canvas_height = 600
Center_Canvas = [Canvas_width/2,Canvas_height/2]

# Create Canvas
canvas = Canvas(width=Canvas_width, height= Canvas_height, bg='gray')  
canvas.grid(row=0, column=0 , columnspan = 8, padx=5)


Background_color = ["Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White"]
Color_Label =[None]*8

current_color = ["White"]

for i in range(0,2):
    for j in range(0,8):
        Color_Label[j] = Label(root,text="", bg= Background_color[j], borderwidth=1,relief="solid",padx=20)
        Color_Label[j].grid(row= i+1, column=j,pady=2)   
        Color_Label[j].bind("<Button-1>", lambda e, c=Background_color[j]:printatore(c))
        print(Color_Label[j].cget("bg"))


def printatore(color_print):
    print(color_print)
    current_color[0] = color_print
    return current_color


#Red_Color = Label(root,text="", bg="#c50f1f", borderwidth=1,relief="solid")
#Red_Color.grid(row=1, column=1,sticky=W+E, padx=5, ipadx=10)

row = 20
column = 20
pixel_size = 30

def createMatrix(row, col):
    mat = []
    for el in range(row):
        mat.append([3]*20)
    return mat


Color_Grid = createMatrix(20, 20)
print(Color_Grid)

def Save_Matrix():
    print("save")


def draw_pixel(row,column,color,pixel_size,cordx,cordy):
      #print(row,column,color)
      #cordy = (row) * pixel_size
      #cordx = (column) * pixel_size
      print(cordx)
      print(cordy)
      cordx = math.floor(cordx/30) * 30
      cordy = math.floor(cordy/30) * 30
      print(cordx)
      print(cordy)
      
      Color_Grid[math.floor(cordy/30)][math.floor(cordx/30)] = color
      
      print(Color_Grid)
      print("\n")
      print(Color_Grid[1])
      print("\n")
      print(Color_Grid[2])
      #print(str(row) + " " + str(column))
      if color == '0':
        color = "white"
      canvas.create_rectangle(cordx, cordy, cordx + pixel_size, cordy + pixel_size , width = 0, fill = color , tags="pixel")
      #canvas.create_rectangle(0, 0, 30,30, width = 0, fill = color , tags="pixel")
      #pixel_color[row][column] = color
      
      open('demofile.txt', 'w').close()
      for el in range(len(Color_Grid)):
        with open("demofile.txt", "a") as f:
            f.write(", ".join(str(x) for x in Color_Grid[el])+ "\n")
            #f.write(str(Color_Grid[el])+"\n")  

def mostra_coordinate(event):
    # event.x e event.y contengono le coordinate relative al Canvas
    draw_pixel(30,30,current_color[0],30,event.x,event.y)   #row,column, 
    print(f"Click a: x={event.x}, y={event.y}")
    
    
# Collega il click del mouse (tasto sinistro) alla funzione
canvas.bind("<Button-1>", mostra_coordinate)

root.mainloop()
