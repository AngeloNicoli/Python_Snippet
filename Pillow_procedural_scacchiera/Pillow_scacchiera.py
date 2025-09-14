from PIL import Image, ImageDraw
import random

def scacchiera_colori(dim, num_blocchi):
    img = Image.new("RGB", (dim, dim))
    draw = ImageDraw.Draw(img)

    blocco = dim // num_blocchi
    for y in range(num_blocchi):
        for x in range(num_blocchi):
            colore = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            draw.rectangle(
                [x * blocco, y * blocco, (x + 1) * blocco, (y + 1) * blocco],
                fill=colore
            )
    return img

img = scacchiera_colori(512, 16)
img.show()
img.save("scacchiera_colorata.png")