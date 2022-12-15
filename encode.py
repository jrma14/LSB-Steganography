# encodes a message into an image using the LSB method

import sys
from PIL import Image

max_size = 32


def encode(image, message):
    # encode the message into the image
    # image is the image to encode the message into
    # message is the message to encode into the image
    # returns the encoded image

    # convert the image to RGB if it isn't already
    image = image.convert("RGB")

    # convert the message to binary
    binary = ''.join([format(ord(i), "08b") for i in message])

    length = len(message)
    for i in range(max_size):
        binary = str((length >> i & 1)) + binary

    # print(len(binary), " bits to encode")
    # print(binary)

    # get the width and height of the image
    width, height = image.size
    # check if the message is too long to be encoded
    if len(binary) > (width * height * 3) or len(binary) > 2 ** (max_size - 1):
        raise Exception(
            "The message is too long to be encoded into this image.")

    # encode the message into the image
    # the message is encoded into the least significant bit of each pixel
    index = 0
    length = len(message)
    for row in range(height):
        for col in range(width):
            # get the RGB values of the pixel
            pixel = list(image.getpixel((col, row)))
            # set the LSB of each value to the next bit of the message
            for i in range(3):
                if index < len(binary):
                    pixel[i] = pixel[i] & ~1 | int(binary[index])
                    # & ~1 sets the LSB to 0
                    # | int(binary[index]) sets the LSB to the next bit of the message
                    index += 1
                else:
                    image.putpixel((col, row), (tuple(pixel)))
                    return image

            # set the pixel to the new value
            image.putpixel((col, row), (tuple(pixel)))

    return image


def main():
    print("Encoding...")
    # get the image and message from the command line arguments
    image = Image.open("yoda.png")
    message = "No! Try not. Do. Or do not. There is no try. Hrrmmm. Seeing this if you are, us a B please give."

    # encode the message into the image
    encoded = encode(image, message)

    # save the encoded image
    encoded.save("./encoded.png", quality=100)

    print("Done!")


if __name__ == "__main__":
    main()
