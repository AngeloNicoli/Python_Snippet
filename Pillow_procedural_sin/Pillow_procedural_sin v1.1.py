from PIL import Image
import math

def genera_pattern_sinusoide(dim):
    img = Image.new("RGB", (dim, dim))
    pixels = img.load()

    for y in range(dim):
        for x in range(dim):
            # Valore da 0 a 255 basato su una funzione seno
            val = (int((math.sin(x * 0.05 + y * 0.05) + 1) / 2 * 255))
            #val = (int((math.sin(x * 0.2) + 1) / 2 * 255))
            val2 = (int((math.sin(x * 0.5 + y * 0.5) + 1) / 2 * 255))
            #print(val)
            pixels[x, y] = (val,val2, val)

    return img

img = genera_pattern_sinusoide(1024)
img.show()
name_file = input("scegli un nome per saldare l'immagine")
img.save(name_file + ".png")
