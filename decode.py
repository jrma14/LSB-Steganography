# this script decodes an image that has been encoded using the LSB method

import sys
from PIL import Image

max_size = 32


def decode(image):
    # decode the message from the image
    # image is the image to decode the message from
    # returns the decoded message

    # convert the image to RGB if it isn't already
    image = image.convert("RGB")

    # get the width and height of the image
    width, height = image.size

    messageBinary = ""
    index = 0
    length = 0
    for row in range(height):
        for col in range(width):
            # print(row)
            # get the RGB values of the pixel
            pixel = list(image.getpixel((col, row)))

            # get the LSB of each value and add it to the message
            for value in pixel[:3]:
                if index <= max_size - 1:
                    length <<= 1
                    length += value & 1
                elif index < length * 8 + max_size:
                    messageBinary += str(value & 1)
                else:
                    break
                index += 1

            # check if we have reached the end of the message
            # if endOfMessageIndicatorBinary in messageBinary[-480:]:
            # remove the end of message indicator from the message
    # messageBinary = messageBinary[:-
    # len(endOfMessageIndicatorBinary)]

    # convert the binary message to a string
    message = "".join(
        [chr(int(messageBinary[i:i + 8], 2)) for i in range(0, len(messageBinary), 8)])

    return message[:length]


def main():
    image = Image.open("./encoded.png")

    print("Decoding image...")

    # decode the message from the image
    message = decode(image)

    # print the decoded message
    print(message)


if __name__ == "__main__":
    main()
