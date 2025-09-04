from tkinter import *

# Size of Main Window
window_width = 610
window_height = 700

# Create Main Window
root = Tk()
root.geometry(str(window_width) + "x" + str(window_height))
root.title("Map Drawer")
# root.configure(bg="white")

# Size of Canvas
Canvas_width = 600
Canvas_height = 600
Center_Canvas = [Canvas_width/2,Canvas_height/2]

# Create Canvas
canvas = Canvas(width=Canvas_width, height= Canvas_height, bg='gray')  
canvas.grid(row=0, column=0 , columnspan = 8, padx=5)

Background_color = ["Green", "Red", "Blue", "Red", "Green", "Red", "Green", "Red"]


for i in range(0,2):
    for j in range(0,7):
        Color_01 = Label(root,text="", bg= Background_color[j], borderwidth=1,relief="solid",padx=20)
        Color_01.grid(row= i+1, column=j,pady=2)   


def printatore():
    print("3")


Color_01.bind("<Button-1>", lambda e:printatore())

   
#Red_Color = Label(root,text="", bg="#c50f1f", borderwidth=1,relief="solid")
#Red_Color.grid(row=1, column=1,sticky=W+E, padx=5, ipadx=10)

row = 20
column = 20
pixel_size = 20

def draw_pixel(row,column,color):
      #print(row,column,color)
      cordy = (row) * pixel_size
      cordx = (column) * pixel_size
      #print(str(row) + " " + str(column))
      if color == '0':
         color = "white"
      Pages[canvas_page-1].create_rectangle(cordx, cordy, cordx + pixel_size, cordy + pixel_size , width = 0, fill = color , tags="pixel")
      pixel_color[row][column] = color


def mostra_coordinate(event):
    # event.x e event.y contengono le coordinate relative al Canvas
    print(f"Click a: x={event.x}, y={event.y}")


# Collega il click del mouse (tasto sinistro) alla funzione
canvas.bind("<Button-1>", mostra_coordinate)



root.mainloop()
