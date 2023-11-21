from PNGToArray import getMapArray
from getPNGAndHTML import downloadHTMLAndMapImage
from animatedToArray import getGIFName
import os

pathToMap = 'AWBW-Map-Reader/saved/map.png'

##If the files don't exist, download them through url
if not os.path.exists(pathToMap):
    url = input("Input the url to the map preview: ")
    downloadHTMLAndMapImage(url)
else:
    url = input("Input the url to the map preview, or leave blank to use the previous url: ")
    if url != "":
        downloadHTMLAndMapImage(url)

#Create the map array
mapArray = getMapArray()

#mapArray still has 'empty' tiles. Use getGIFName to fill in the rest.
for i in range(len(mapArray)):
    for j in range(len(mapArray[i])):
        if mapArray[i][j] == 'empty':
            tile = getGIFName(j, i)
            if tile is not None:
                mapArray[i][j] = tile


def printArray(array):
    max_lengths = [max(map(len, col)) for col in zip(*array)]

    # Print the 2D array with proper alignment
    for row in array:
        for element, length in zip(row, max_lengths):
            print(element.ljust(length + 2), end='')  # Add 2 for extra spacing between columns
        print()

printArray(mapArray)