from PIL import Image, ImageFilter
import random

# Dimensione texture
width, height = 256, 256
block_size = 16  # Dimensione delle "chiazze"

# Palette di colori roccia
rock_colors = [
    (100, 100, 100),
    (120, 110, 100),
    (80, 80, 80),
    (130, 120, 110),
    (90, 85, 80),
]

# Crea nuova immagine RGB
img = Image.new("RGB", (width, height))

# Disegna per blocchi
for by in range(0, height, block_size):
    for bx in range(0, width, block_size):
        # Colore base della chiazza
        base_color = random.choice(rock_colors)
        # Piccola variazione casuale
        variation = random.randint(-10, 10)
        r = min(255, max(0, base_color[0] + variation))
        g = min(255, max(0, base_color[1] + variation))
        b = min(255, max(0, base_color[2] + variation))
        color = (r, g, b)

        # Riempi il blocco con quel colore
        for y in range(by, min(by + block_size, height)):
            for x in range(bx, min(bx + block_size, width)):
                img.putpixel((x, y), color)

# Applica un blur per ammorbidire i bordi tra le chiazze
img = img.filter(ImageFilter.GaussianBlur(radius=2))

# Salva e mostra
img.save("roccia_chiazze_grandi.png")
img.show()
