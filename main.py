# Jeff Wilson

import cv2
import numpy


def two_level_gray_encoding(imageArr, width, height):
    # Number of Pixels in the image
    # Check each pixel in the numpy array. Split into the two gray levels
    for x in range(width):
        for y in range(height):
            if 0 <= imageArr[x, y] <= 127:
                imageArr[x, y] = 0
            elif 128 <= imageArr[x, y] <= 255:
                imageArr[x, y] = 1


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


def fifteen_level_gray_encoding(imageArr, width, height):
    # Number of Pixels in the image
    # Check each pixel in the numpy array. Split into the two gray levels
    for x in range(width):
        for y in range(height):
            if 0 <= imageArr[x, y] <= 16:
                imageArr[x, y] = 0
            elif 17 <= imageArr[x, y] <= 34:
                imageArr[x, y] = 1
            elif 35 <= imageArr[x, y] <= 52:
                imageArr[x, y] = 2
            elif 53 <= imageArr[x, y] <= 70:
                imageArr[x, y] = 3
            elif 71 <= imageArr[x, y] <= 88:
                imageArr[x, y] = 4
            elif 89 <= imageArr[x, y] <= 106:
                imageArr[x, y] = 5
            elif 107 <= imageArr[x, y] <= 124:
                imageArr[x, y] = 6
            elif 125 <= imageArr[x, y] <= 142:
                imageArr[x, y] = 7
            elif 143 <= imageArr[x, y] <= 160:
                imageArr[x, y] = 8
            elif 161 <= imageArr[x, y] <= 178:
                imageArr[x, y] = 9
            elif 179 <= imageArr[x, y] <= 196:
                imageArr[x, y] = 10
            elif 197 <= imageArr[x, y] <= 214:
                imageArr[x, y] = 11
            elif 215 <= imageArr[x, y] <= 232:
                imageArr[x, y] = 12
            elif 233 <= imageArr[x, y] <= 250:
                imageArr[x, y] = 13
            elif 251 <= imageArr[x, y] <= 255:
                imageArr[x, y] = 14


def fifteen_level_gray_decoding(imageArr, width, height):
    for x in range(width):
        for y in range(height):
            if imageArr[x, y] == 0:
                imageArr[x, y] = 8
            elif imageArr[x, y] == 1:
                imageArr[x, y] = 25
            elif imageArr[x, y] == 2:
                imageArr[x, y] = 43
            elif imageArr[x, y] == 3:
                imageArr[x, y] = 61
            elif imageArr[x, y] == 4:
                imageArr[x, y] = 79
            elif imageArr[x, y] == 5:
                imageArr[x, y] = 97
            elif imageArr[x, y] == 6:
                imageArr[x, y] = 115
            elif imageArr[x, y] == 7:
                imageArr[x, y] = 133
            elif imageArr[x, y] == 8:
                imageArr[x, y] = 151
            elif imageArr[x, y] == 9:
                imageArr[x, y] = 169
            elif imageArr[x, y] == 10:
                imageArr[x, y] = 177
            elif imageArr[x, y] == 11:
                imageArr[x, y] = 205
            elif imageArr[x, y] == 12:
                imageArr[x, y] = 223
            elif imageArr[x, y] == 13:
                imageArr[x, y] = 241
            elif imageArr[x, y] == 14:
                imageArr[x, y] = 253


def generate_error_image(error_arr, orig_image, decoded_image, width, height):
    max_val = 1
    for x in range(width):
        for y in range(height):
            value = abs(int(orig_image[x, y]) - int(decoded_image[x, y]))
            if value > max_val:
                max_val = value
            error_arr[x, y] = value

    return max_val


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

# Generate Header
max_value = 191
pgmHeader = 'P5' + '\n' + str(width) + ' ' + str(height) + '\n' + str(max_value) + '\n' + '\n'
pgmHeader_byte = bytearray(pgmHeader, 'utf-8')
filename = "baboon2-levels-R.pgm"

# Decode
two_level_gray_decoding(image_2_Gray, width, height)
print('Printing Image: ' + str(filename))
cv2.imwrite(filename, image_2_Gray)

# Replace header in generated .pgm file
with open(filename, "r+b") as file:
    file.write(pgmHeader_byte)
file.close()


# Start 15 Gray Level Encoding Process

# Generate Header
max_value = 14
pgmHeader = 'P5' + '\n' + str(width) + ' ' + str(height) + '\n' + str(max_value) + '\n' + '\n'
pgmHeader_byte = bytearray(pgmHeader, 'utf-8')
filename = "baboon15-levels.pgm"

# Encode
fifteen_level_gray_encoding(image_15_Gray, width, height)
array_out = numpy.array(image_15_Gray)
print('Printing Image: ' + str(filename))
cv2.imwrite(filename, image_15_Gray)

# Replace header in generated .pgm file
with open(filename, "r+b") as file:
    file.write(pgmHeader_byte)
file.close()

# Start 15 Gray Level Decoding Process

# Generate Header
max_value = 253
pgmHeader = 'P5' + '\n' + str(width) + ' ' + str(height) + '\n' + str(max_value) + '\n' + '\n'
pgmHeader_byte = bytearray(pgmHeader, 'utf-8')
filename = "baboon15-levels-R.pgm"

# Decode
fifteen_level_gray_decoding(image_15_Gray, width, height)
print('Printing Image: ' + str(filename))
cv2.imwrite(filename, image_15_Gray)

# Replace header in generated .pgm file
with open(filename, "r+b") as file:
    file.write(pgmHeader_byte)
file.close()

# Error Image Processing for 2 Levels
image_2_Error = image_original
image_2_Encoded = cv2.imread('baboon2-levels.pgm', -1)
image_2_Decoded = cv2.imread('baboon2-levels-R.pgm', -1)

max_value = generate_error_image(image_2_Error, image_original, image_2_Decoded, width, height)

pgmHeader = 'P5' + '\n' + str(width) + ' ' + str(height) + '\n' + str(max_value) + '\n' + '\n'
pgmHeader_byte = bytearray(pgmHeader, 'utf-8')
filename = "baboon2-levels-ERROR.pgm"

print('Printing Image: ' + str(filename))
cv2.imwrite(filename, image_2_Error)

# Replace header in generated .pgm file
with open(filename, "r+b") as file:
    file.write(pgmHeader_byte)
file.close()


# Error Image Processing for 15 Levels
image_15_Error = image_original
image_15_Encoded = cv2.imread('baboon15-levels.pgm', -1)
image_15_Decoded = cv2.imread('baboon15-levels-R.pgm', -1)

max_value = generate_error_image(image_15_Error, image_original, image_15_Decoded, width, height)

pgmHeader = 'P5' + '\n' + str(width) + ' ' + str(height) + '\n' + str(max_value) + '\n' + '\n'
pgmHeader_byte = bytearray(pgmHeader, 'utf-8')
filename = "baboon15-levels-ERROR.pgm"

print('Printing Image: ' + str(filename))
cv2.imwrite(filename, image_15_Error)

# Replace header in generated .pgm file
with open(filename, "r+b") as file:
    file.write(pgmHeader_byte)
file.close()



