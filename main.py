# Jeff Wilson

import cv2
import numpy


def two_level_gray_encoding(imageArr, width, height):
    # Number of Pixels in the image
    # Check each pixel in the numpy array. Split into the two gray levels
    for x in range(width):
        for y in range(height):
            if 0 <= imageArr[x, y] <= 127:
                # print('Pixel: ' + str(x) + ', ' + str(y) + ' set to 0! \n')
                imageArr[x, y] = 0
                # fout.write(bytearray(0))
            elif 128 <= imageArr[x, y] <= 255:
                # print('Pixel: ' + str(x) + ', ' + str(y) + ' set to 1! \n')
                imageArr[x, y] = 1
                # fout.write(bytearray(1))


def two_level_gray_decoding(imageArr, width, height):
    # Check each pixel in the numpy array.
    # If it is 0, set to 63 (Midpoint of range from encoding)
    # If it is 1, set to 191.
    for x in range(width):
        for y in range(height):
            if imageArr[x, y] == 0:
                imageArr[x, y] = 63
            elif imageArr[x, y] == 1:
                imageArr[x, y] = 191


# Read .pgma image into Numpy Array
image_original = cv2.imread('baboon.pgma', -1)
image_2_Gray = cv2.imread('baboon.pgma', -1)
image_15_Gray = cv2.imread('baboon.pgma', -1)

height, width = image_original.shape


# Note to Self: Result of loading with cv2 is a Numpy Array!
print('--- Image Properties --- \n')
print('Type: ' + str(type(image_original)) + '\n')

# Summarize shape
print('Shape: ' + str(image_original.shape) + '\n')

# Start 2 Gray Level Encoding Process
# Generate Header
max_value = 1
pgmHeader = 'P5' + '\n' + str(width) + ' ' + str(height) + '\n' + str(max_value) + '\n' + '\n'
pgmHeader_byte = bytearray(pgmHeader, 'utf-8')
filename = "baboon2-levels.pgm"

# Encode
two_level_gray_encoding(image_2_Gray, width, height)
array_out = numpy.array(image_2_Gray)
print('Printing Image: ' + str(filename))
cv2.imwrite(filename, image_2_Gray)

# Replace header in generated .pgm file
with open(filename, "r+b") as file:
    file.write(pgmHeader_byte)

file.close()

# Start 2 Gray Level Decoding Process
max_value = 191
pgmHeader = 'P5' + '\n' + str(width) + ' ' + str(height) + '\n' + str(max_value) + '\n' + '\n'
pgmHeader_byte = bytearray(pgmHeader, 'utf-8')
filename = "baboon2-levels-R.pgm"

two_level_gray_decoding(image_2_Gray, width, height)
print('Printing Image: ' + str(filename))
cv2.imwrite(filename, image_2_Gray)

with open(filename, "r+b") as file:
    file.write(pgmHeader_byte)

file.close()




