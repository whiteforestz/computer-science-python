from PIL import Image, ImageFilter


# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html

def image_open(file: str) -> Image.Image:
    return Image.open(file)


im = image_open('img.png')

blur_im = im.filter(ImageFilter.BoxBlur(25))

blur_im.show()
