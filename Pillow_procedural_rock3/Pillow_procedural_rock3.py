from PIL import Image, ImageFilter, ImageDraw
import random

# Dimensione texture
width, height = 256, 256
block_size = 16

# Palette di colori roccia
rock_colors = [
    (100, 100, 100),
    (120, 110, 100),
    (80, 80, 80),
    (130, 120, 110),
    (90, 85, 80),
]

# Crea immagine base con chiazze grandi
img = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(img)

for by in range(0, height, block_size):
    for bx in range(0, width, block_size):
        base_color = random.choice(rock_colors)
        variation = random.randint(-10, 10)
        r = min(255, max(0, base_color[0] + variation))
        g = min(255, max(0, base_color[1] + variation))
        b = min(255, max(0, base_color[2] + variation))
        color = (r, g, b)

        for y in range(by, min(by + block_size, height)):
            for x in range(bx, min(bx + block_size, width)):
                img.putpixel((x, y), color)

# Leggero blur
img = img.filter(ImageFilter.GaussianBlur(radius=1.5))

# === CREPE SPEZZATE ===
num_crepe = 20
for _ in range(num_crepe):
    # Partenza casuale
    x, y = random.randint(0, width-1), random.randint(0, height-1)
    # Numero di segmenti della crepa
    segments = random.randint(10, 30)
    # Spessore casuale
    thickness = random.randint(1, 2)

    for _ in range(segments):
        # Direzione randomizzata (leggero spostamento)
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        x2 = max(0, min(width - 1, x + dx))
        y2 = max(0, min(height - 1, y + dy))

        # Colore crepa (scurissimo)
        vein_color = (20, 20, 20)

        # Disegna segmento
        draw.line((x, y, x2, y2), fill=vein_color, width=thickness)

        # Prossimo punto
        x, y = x2, y2

# Salva e mostra
img.save("roccia_crepe_fratturate.png")
img.show()
