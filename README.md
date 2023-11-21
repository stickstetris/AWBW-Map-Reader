# AWBW Map Reader

Creates a 2D array in python of an AWBW map, given its map preview url.

![image_2023-11-19_230723225](https://github.com/stickstetris/AWBW-Map-Reader/assets/151409707/0608ec8d-4b23-410f-a076-609d38ae5e41)


```
Input the url to the map preview, or leave blank to use the previous url: https://awbw.amarriner.com/prevmaps.php?maps_id=153739
HTML content saved to AWBW-Map-Reader\saved\html_content.txt
Image downloaded and saved to AWBW-Map-READER/saved/map.png
mountain       plain            forest        road2           road2
ocean3         shoal            pipe2         pipe            brokenpipe    
silo           base_orangestar  base_neutral  base_bluemoon   base_neutral
plain          plain            reef          plain           plain
hq_orangestar  plain            plain         lab_orangestar  hq_bluemoon
```
### Prerequisites

Python 3.11.6 or later
Libraries:
requests 2.31.0 or later
beautifulsoup4 4.12.2 or later
opencv-python 4.8.1.78 or later

```
pip install requests
pip install beautifulsoup4
pip install opencv-python
```
