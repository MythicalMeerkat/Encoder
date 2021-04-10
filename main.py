# Jeff Wilson

import cv2
import numpy


def two_level_gray_encoding(imageArr, width, height):
    # Number of Pixels in the image
    total_pixels = width * height
    #filename = "baboon2-levels.pgm"

    #fout = open(filename, 'wb')
    #pgmHeader = 'P5' + '\n' + str(width) + ' ' + str(height) + '\n' + str(1) + '\n'
    #pgmHeader_byte = bytearray(pgmHeader, 'utf-8')

    #fout.write(pgmHeader_byte)


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
max_value = 1
two_level_gray_encoding(image_2_Gray, width, height)
array_out = numpy.array(image_2_Gray)
filename = "baboon2-levels.pgm"
print('Printing Image: ' + str(filename))
cv2.imwrite(filename, image_2_Gray)

pgmHeader = 'P5' + '\n' + str(width) + ' ' + str(height) + '\n' + str(1) + '\n' + '\n'
pgmHeader_byte = bytearray(pgmHeader, 'utf-8')
with open(filename, "r+b") as file:
    file.write(pgmHeader_byte)




