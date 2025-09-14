from PIL import Image, ImageDraw
import random

# Dimensioni della texture
width, height = 512, 512

# Crea immagine verde scuro di base
img = Image.new("RGB", (width, height), (20, 70, 20))
draw = ImageDraw.Draw(img)

# Disegna "fili d'erba" con variazioni di verde
for _ in range(10000):
    x = random.randint(0, width)
    y = random.randint(0, height)
    length = random.randint(3, 7)
    angle = random.uniform(-0.5, 0.5)
    green_shade = random.randint(80, 180)
    color = (20, green_shade, 20)
    
    # Simula un filo d'erba come una linea
    draw.line(
        [(x, y), (x + angle * length, y - length)],
        fill=color,
        width=1
    )

img.show()
img.save("texture_erba.png")