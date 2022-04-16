from PIL import Image


def check_image_size(image: Image) -> bool:
    """Check if image width and height are divisible by 8"""
    return image.size[0] % 8 == 0 and image.size[1] % 8 == 0


def change_image_size(image: Image) -> Image:
    """Returns an Image with width and height divisible by 8"""
    width, height = image.size
    new_width = width // 8 * 8 + 8
    new_heigth = height // 8 * 8 + 8

    return image.resize((new_width, new_heigth))


image = Image.open("nico.jpg")
# image = Image.open("face1.png")
# image = Image.open("medium.bmp")

if not check_image_size(image):
    image = change_image_size(image)

ycbcr_image = image.convert("YCbCr")
print(ycbcr_image.getbands())
ycbcr_image.show()