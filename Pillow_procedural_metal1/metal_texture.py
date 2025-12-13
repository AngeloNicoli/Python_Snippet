from PIL import Image, ImageFilter
import random

def generate_metal_texture(width=800, height=600, intensity=50):
    # Crea immagine in scala di grigi con rumore
    img = Image.new("L", (width, height))
    pixels = img.load()

    # Rumore orizzontale tipo "brushed"
    for y in range(height):
        line_noise = random.randint(100 - intensity, 155 + intensity)
        for x in range(width):
            # Aggiunge variazioni minime tra i pixel per simulare l'effetto spazzolato
            pixels[x, y] = line_noise + random.randint(-8, 8)

    # Applica un motion blur orizzontale
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    img = img.filter(ImageFilter.BoxBlur(3))

    return img

if __name__ == "__main__":
    texture = generate_metal_texture(1024, 1024, intensity=60)
    texture.save("metal_texture.png")
    texture.show()
