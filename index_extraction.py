from skimage import data, io
from PIL import Image
import numpy
import csv



image = numpy.array(Image.open('image_country_G04L02.tif'))

print(image.shape)


pixel_indexes = {}
for i in range(40, 531):
    for j in range(25, 524):
        value = image[i][j][0] == 0 and image[i][j][1] == 0 and image[i][j][2] == 0 or (image[i][j][0] == 255 and image[i][j][1] == 255 and image[i][j][2] == 255)
        if value == False and (
                (image[i][j][0] >= 10 and image[i][j][1] <= 8 and image[i][j][2] <= 8) == False):
                pixel_indexes[(i, j)] = image
        else:
            print(str(j))
file = open('indexes.csv', 'w')

csv_writer = csv.writer(file, delimiter=',')
for (i, j) in pixel_indexes.keys():
    csv_writer.writerow([i, j])

for i in range(40, 531):
    for j in range(25, 524):
        if (i, j) in pixel_indexes:
            image[i][j][1] = 255
            image[i][j][0] = 0
            image[i][j][2] = 0
image_sk_raw = image[40:531, 25:524]
io.imshow(image_sk_raw)
io.show()