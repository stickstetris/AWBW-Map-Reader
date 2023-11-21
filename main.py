from PNGToArray import getMapArray
from getPNGAndHTML import downloadHTMLAndMapImage
from animatedToArray import getGIFName
import os

pathToMap = 'AWBW-Map-Reader\saved\map.png'

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


print(mapArray)