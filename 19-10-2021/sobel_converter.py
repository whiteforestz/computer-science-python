import math

from PIL import Image, ImageDraw

G_X = [
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1],
]

G_Y = [
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1],
]


def image_open(file: str) -> Image.Image:
    return Image.open(file)


def to_gray(color: tuple) -> int:
    (r, g, b, _) = color
    return (r + g + b) // 3


def to_sobel_pixel(pos_xy: tuple, image_pixels, g: list) -> int:
    (pos_x, pos_y) = pos_xy

    sobel_pixel = 0
    sobel_pixel += g[0][0] * to_gray(image_pixels[pos_x - 1, pos_y - 1])
    sobel_pixel += g[0][1] * to_gray(image_pixels[pos_x, pos_y - 1])
    sobel_pixel += g[0][2] * to_gray(image_pixels[pos_x + 1, pos_y - 1])

    sobel_pixel += g[1][0] * to_gray(image_pixels[pos_x - 1, pos_y])
    sobel_pixel += g[1][1] * to_gray(image_pixels[pos_x, pos_y])
    sobel_pixel += g[1][2] * to_gray(image_pixels[pos_x + 1, pos_y])

    sobel_pixel += g[2][0] * to_gray(image_pixels[pos_x - 1, pos_y + 1])
    sobel_pixel += g[2][1] * to_gray(image_pixels[pos_x, pos_y + 1])
    sobel_pixel += g[2][2] * to_gray(image_pixels[pos_x + 1, pos_y + 1])

    return sobel_pixel


im = image_open('img.png')
(width, height) = im.size
pixels = im.load()

sobel_im = Image.new(im.mode, im.size)
drawer = ImageDraw.Draw(sobel_im)

for x in range(1, width - 1):
    for y in range(1, height - 1):
        pixel_x = to_sobel_pixel((x, y), pixels, G_X)
        pixel_y = to_sobel_pixel((x, y), pixels, G_Y)

        pixel = min(int(math.sqrt(pixel_x**2 + pixel_y**2)), 255)
        drawer.point((x, y), (pixel, pixel, pixel))

sobel_im.show()
