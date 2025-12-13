from PIL import Image, ImageFilter, ImageOps, ImageChops
import random
import math

def generate_brushed_noise(width, height, noise_intensity=30):
    """Genera rumore tipo brushed metal."""
    img = Image.new("L", (width, height))
    px = img.load()

    for y in range(height):
        base = random.randint(110 - noise_intensity, 145 + noise_intensity)
        for x in range(width):
            px[x, y] = base + random.randint(-5, 5)

    # Leggero motion blur orizzontale
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    img = img.filter(ImageFilter.BoxBlur(2))
    return img


def add_radial_highlight(img, strength=0.6):
    """Aggiunge un riflesso centrale radiale (look metallico realistico)."""
    width, height = img.size
    center = (width / 2, height / 2)

    highlight = Image.new("L", (width, height))
    px = highlight.load()

    for y in range(height):
        for x in range(width):
            d = math.dist((x, y), center)
            max_d = math.dist((0, 0), center)
            v = max(0, 255 - int((d / max_d) * 255 * (1 - strength)))
            px[x, y] = v

    return ImageChops.screen(img, highlight)


def apply_color(img, color=(200, 200, 200)):
    """Colora la texture (RGB) preservando la luminanza."""
    return ImageOps.colorize(img, black=(0, 0, 0), white=color)


def make_tileable(img):
    """Rende l'immagine seamless."""
    w, h = img.size

    # Shift per evitare bordi visibili
    img = ImageChops.offset(img, w//2, h//2)
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    img = ImageChops.offset(img, -w//2, -h//2)
    return img


def generate_metal_texture(
        width=1024,
        height=1024,
        color=(180, 180, 190),   # acciaio
        noise_intensity=10,
        highlight_strength=0.6
    ):

    img = generate_brushed_noise(width, height, noise_intensity)
    img = make_tileable(img)
    img = add_radial_highlight(img, strength=highlight_strength)
    img = apply_color(img, color)
    return img


if __name__ == "__main__":
    texture = generate_metal_texture(
        1024, 1024,
        #color=(255, 220, 120),    # prova: oro
        color=(180, 180, 190),     # acciaio inox
        #color=(200, 200, 200),   # acciaio
        noise_intensity=50,
        highlight_strength=0.7
    )

    texture.save("metal_texture_realistic_tileable.png")
    texture.show()
