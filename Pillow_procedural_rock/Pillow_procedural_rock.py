from PIL import Image, ImageFilter
import random

# Dimensione texture
width, height = 256, 256

# Palette di colori roccia (grigi e marroni)
rock_colors = [
    (100, 100, 100),  # grigio medio
    (120, 110, 100),  # grigio-marrone
    (80, 80, 80),     # grigio scuro
    (130, 120, 110),  # roccia chiara
    (90, 85, 80),     # tono spento
]

# Crea immagine vuota
img = Image.new("RGB", (width, height))

# Disegna pixel
for y in range(height):
    for x in range(width):
        # Scegli un colore casuale dalla palette
        color = random.choice(rock_colors)

        # Applica una piccola variazione
        variation = random.randint(-10, 10)
        r = min(255, max(0, color[0] + variation))
        g = min(255, max(0, color[1] + variation))
        b = min(255, max(0, color[2] + variation))

        img.putpixel((x, y), (r, g, b))

# Applica blur per rendere le transizioni meno “pixelate”
img = img.filter(ImageFilter.GaussianBlur(radius=1.2))

# Salva e mostra
img.save("roccia_texture.png")
img.show()
