from PIL import Image
import random

# Dimensione della texture
width, height = 256, 256

# Colore base sabbia
base_color = (210, 180, 140)  # Beige sabbia (RGB)

# Percentuali di granuli
white_grain_chance = 0.015  # 1.5% di pixel
dark_grain_chance = 0.015   # 1.5% di pixel

# Crea nuova immagine RGB
img = Image.new("RGB", (width, height))

# Crea pixel sabbiosi
for y in range(height):
    for x in range(width):
        # Variazione casuale del colore base
        variation = random.randint(-15, 15)
        r = min(255, max(0, base_color[0] + variation))
        g = min(255, max(0, base_color[1] + variation))
        b = min(255, max(0, base_color[2] + variation))
        color = (r, g, b)

        # Decidi se inserire un granulo bianco o nero
        rand = random.random()
        if rand < white_grain_chance:
            color = (255, 255, 255)  # Granulo chiaro
        elif rand < white_grain_chance + dark_grain_chance:
            dark = random.randint(10, 50)
            color = (dark, dark, dark)  # Granulo scuro

        # Applica il pixel
        img.putpixel((x, y), color)

# Salva e mostra
img.save("sabbia_con_granuli.png")
img.show()