#Given a png of a map, returns a 2D array of the map.
import cv2
import numpy as np

def divide_into_tiles(image, tile_size):
    """
    Divide an image into tiles of a specified size.
    """
    height, width, _ = image.shape
    rows = height // tile_size
    cols = width // tile_size

    tiles = []

    for i in range(rows):
        for j in range(cols):
            tile = image[i * tile_size: (i + 1) * tile_size, j * tile_size: (j + 1) * tile_size]
            tiles.append(tile)

    return tiles, rows, cols

def compare_tiles(tile, reference_tiles):
    """
    Compare a tile with a set of reference tiles.
    Return the name of the best-matching tile.
    """
    best_match_name = ""
    best_match_score = float('-inf')  # Initialize with a low value for correlation

    for tile_name, reference_tile in zip(['bridge', 'empty', 'forest', 'mountain', 'ocean', 'ocean2', 'pipe', 'pipe2', 'plain', 'river', 'road', 'road2', 'shoal'], reference_tiles):
        hist_comparison = cv2.compareHist(cv2.calcHist([tile], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256]),
                                          cv2.calcHist([reference_tile], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256]),
                                          cv2.HISTCMP_CORREL)

        if hist_comparison > best_match_score:
            best_match_score = hist_comparison
            best_match_name = tile_name

    return best_match_name

def map_tiles_to_array(tiles, rows, cols, reference_tiles):
    """
    Map tiles to a 2D array based on comparison with reference tiles.
    Return an array of tile names.
    """
    tile_map = np.empty((rows, cols), dtype=np.dtype('U10'))

    for i in range(rows):
        for j in range(cols):
            tile_name = compare_tiles(tiles[i * cols + j], reference_tiles)
            tile_map[i, j] = tile_name

    return tile_map


def getMapArray():
    # Load the map image
    map_image = cv2.imread('AWBW-Map-Reader\saved\map.png')

    # Load reference tiles
    bridge = cv2.imread('AWBW-Map-Reader/tiles/bridge.png')
    empty = cv2.imread('AWBW-Map-Reader/tiles/empty.png')
    forest = cv2.imread('AWBW-Map-Reader/tiles/forest.png')
    mountain = cv2.imread('AWBW-Map-Reader/tiles/mountain.png')
    ocean = cv2.imread('AWBW-Map-Reader/tiles/ocean.png')
    ocean2 = cv2.imread('AWBW-Map-Reader/tiles/ocean2.png')
    pipe = cv2.imread('AWBW-Map-Reader/tiles/pipe.png')
    pipe2 = cv2.imread('AWBW-Map-Reader/tiles/pipe2.png')
    plain = cv2.imread('AWBW-Map-Reader/tiles/plain.png')
    river = cv2.imread('AWBW-Map-Reader/tiles/river.png')
    road = cv2.imread('AWBW-Map-Reader/tiles/road.png')
    road2 = cv2.imread('AWBW-Map-Reader/tiles/road2.png')
    shoal = cv2.imread('AWBW-Map-Reader/tiles/shoal.png')
    shoal2 = cv2.imread('AWBW-Map-Reader/tiles/shoal.png')

    reference_tiles = [bridge, empty, forest, mountain, ocean, ocean2, pipe, pipe2, plain, river, road, road2, shoal, shoal2]

    # Set the tile size
    tile_size = 16

    # Divide the map into tiles
    tiles, rows, cols = divide_into_tiles(map_image, tile_size)

    # Map tiles to a 2D array
    tile_map = map_tiles_to_array(tiles, rows, cols, reference_tiles)

    # Print or use the resulting tile map
    return tile_map