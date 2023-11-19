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
    """
    best_match_index = 0
    best_match_score = float('inf')

    for i, reference_tile in enumerate(reference_tiles):
        score = np.sum(np.abs(tile - reference_tile))
        if score < best_match_score:
            best_match_score = score
            best_match_index = i

    return best_match_index

def map_tiles_to_array(tiles, rows, cols, reference_tiles):
    """
    Map tiles to a 2D array based on comparison with reference tiles.
    """
    tile_map = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        for j in range(cols):
            tile_index = compare_tiles(tiles[i * cols + j], reference_tiles)
            tile_map[i, j] = tile_index

    return tile_map

# Load the map image
map_image = cv2.imread('path/to/your/map.png')

# Load reference tiles
reference_tile1 = cv2.imread('path/to/your/reference_tile1.png')
reference_tile2 = cv2.imread('path/to/your/reference_tile2.png')
# Add more reference tiles as needed

reference_tiles = [reference_tile1, reference_tile2]  # Add your reference tiles to this list

# Set the tile size
tile_size = 16

# Divide the map into tiles
tiles, rows, cols = divide_into_tiles(map_image, tile_size)

# Map tiles to a 2D array
tile_map = map_tiles_to_array(tiles, rows, cols, reference_tiles)

# Print or use the resulting tile map
print(tile_map)
