from PIL import Image, ImageDraw
import random

mylist=["white","red","blue","green"]

def esporta(canvas_x,canvas_y,pixel_size):
    image = Image.new("RGB", (canvas_x, canvas_y), "white")
    n_row = canvas_x/pixel_size
    n_column = canvas_y/pixel_size
    for el in range(int(n_row)):
        for ely in range(int(n_column)):
            col = random.choice(mylist)
            print(type(col))
            print(col)
            ImageDraw.Draw(image).rectangle((el* pixel_size, ely* pixel_size, (el* pixel_size)+pixel_size, (ely* pixel_size)+pixel_size), fill=col)
            print("C")
    image.save("rectangles.png")


esporta(600,600,20)

'''
# Create a blank white image
width, height = 400, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Define rectangles and their colors
rectangles = [
    ((0, 0, 200, 200), "red"),       # Top-left
    ((200, 0, 400, 200), "green"),   # Top-right
    ((0, 200, 200, 400), "blue"),    # Bottom-left
    ((200, 200, 400, 400), "yellow") # Bottom-right
]

# Draw rectangles
for coords, color in rectangles:
    color_input=input("choose a color")
    draw.rectangle(coords, fill=color_input)

# Save or show the image
#image.show()       # To open the image in default viewer
image.save("four_rectangles.png")  # To save it to a file'''
