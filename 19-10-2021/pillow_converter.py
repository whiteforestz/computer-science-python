from PIL import Image, ImageDraw


def image_open(file: str) -> Image.Image:
    return Image.open(file)


im = image_open('img.png')
(width, height) = im.size
pixels = im.load()

gray_im = Image.new(im.mode, im.size)
drawer = ImageDraw.Draw(gray_im)

for x in range(0, width):
    for y in range(0, height):
        (r, g, b, a) = pixels[x, y]
        gray = (r + g + b) // 3

        drawer.point((x, y), (gray, gray, gray))

gray_im.show()
