from PIL import Image

def gradiente_radiale(dim):
    img = Image.new("RGB", (dim, dim))
    pixels = img.load()
    center = dim / 2

    for y in range(dim):
        for x in range(dim):
            dx = x - center
            dy = y - center
            dist = (dx**2 + dy**2)**0.5
            val = int(255 * (1 - min(dist / center, 1)))
            pixels[x, y] = (val, val, val)

    return img

img = gradiente_radiale(512)
img.show()
img.save("gradiente_radiale.png")