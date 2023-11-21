import PNGToArray
import getPNGAndHTML
import animatedToArray
import os

pathToMap = 'AWBW-Map-Reader\saved\map.png'
getPNGAndHTML.getBoth('https://awbw.amarriner.com/prevmaps.php?maps_id=153739')

##If the files don't exist, download them through url
if not os.path.exists(pathToMap):
    url = input("Input the url to the map preview")
    getPNGAndHTML.getBoth(url)

#Create the map array with PNGToArray
mapArray = PNGToArray.getMapArray()

#mapArray still has 'empty' tiles. Use animatedToArray to fill in the rest.
for i in range(len(mapArray)):
    for j in range(len(mapArray[i])):
        if mapArray[i][j] == 'empty':
            tile = animatedToArray.findTile(j, i)
            if tile is not None:
                mapArray[i][j] = tile


print(mapArray)