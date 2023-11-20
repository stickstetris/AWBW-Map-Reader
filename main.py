import PNGToArray
import getPNGAndHTML
import os

pathToMap = 'AWBW-Map-Reader\saved\map.png'
if not os.path.exists(pathToMap):
    url = input("Input the url to the map preview")
    getPNGAndHTML.getBoth(url)

print(PNGToArray.getMapArray())