from PIL import Image

# Dimensioni dell'immagine
width, height = 200, 100

# Crea una nuova immagine RGB
img = Image.new('RGB', (width, height))

# Colori
color1 = (255, 0, 0)   # Rosso
color2 = (0, 0, 255)   # Blu

# Accedi ai pixel
pixels = img.load()

# Assegna i colori
for x in range(width):
    for y in range(height):
        if x < width // 2:
            pixels[x, y] = color1
        else:
            pixels[x, y] = color2

# Salva l'immagine in PNG
img.save('due_colori.png')