from PIL import Image
import random

# Dimensione della texture
width, height = 512, 512

# Colore base sabbia
base_color = (210, 180, 140)  # Beige sabbia (RGB)

# Crea nuova immagine RGB
img = Image.new("RGB", (width, height))

# Crea pixel sabbiosi
for y in range(height):
    for x in range(width):
        # Variazione casuale [-15, +15]
        variation = random.randint(-15, 15)
        r = min(255, max(0, base_color[0] + variation))
        g = min(255, max(0, base_color[1] + variation))
        b = min(255, max(0, base_color[2] + variation))
        img.putpixel((x, y), (r, g, b))

# Salva immagine
img.save("sabbia_texture.png")
img.show()