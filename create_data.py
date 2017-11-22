from skimage import data, io
from PIL import Image
import numpy
import csv

image = numpy.array(Image.open('image_country_G04L03.tif'))

def load_indexes(year):
    file = open('indexes.csv', 'r')
    reader = csv.reader(file)

    name = 'data'+ str(year) + '.csv'
    file = open(name, 'w')
    for row in reader:
        x = int(row[0])
        y = int(row[1])
        green = float(2*image[x][y][1]-image[x][y][0]-image[x][y][2])/510.0

        indexes[(x,y)] = green
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow([x, y, green])
indexes = {}

load_indexes('Aug2017')
file = open('indexes.csv', 'r')
reader = csv.reader(file)
for row in reader:
    i = int(row[0])
    j = int(row[1])
    if (i, j) in indexes:
        image[i][j][1] = ((indexes[(i, j)]+1.0)/2.0)*255
        image[i][j][0] = 0
        image[i][j][2] = 0
image_sk_raw = image[40:531, 25:524]
io.imshow(image_sk_raw)
io.show()