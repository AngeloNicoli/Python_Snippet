from PIL import Image, ImageDraw, ImageFilter
import math
import random

# Dimensione texture
width, height = 256, 256

# Crea nuova immagine RGB
img = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(img)

# Parametri per le onde
wave_frequency = 0.04
wave_amplitude = 18

# Colore base acqua
base_color = (20, 60, 160)  # blu scuro

for y in range(height):
    for x in range(width):
        # Calcolo dell'onda (sinusoide disturbata)
        wave = math.sin(x * wave_frequency + random.uniform(-0.3, 0.3)) * wave_amplitude
        brightness = int(30 + wave + random.randint(-15, 15))

        # Applica variazione al colore base
        r = max(0, min(255, base_color[0] + brightness))
        g = max(0, min(255, base_color[1] + brightness))
        b = max(0, min(255, base_color[2] + brightness))

        draw.point((x, y), fill=(r, g, b))

# Applica un blur direzionale (orizzontale) per "ammorbidire le onde"
img = img.filter(ImageFilter.GaussianBlur(radius=1.5))

# Salva e mostra
img.save("acqua_texture.png")
img.show()
