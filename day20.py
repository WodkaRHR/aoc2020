import numpy as np
from collections import defaultdict
from itertools import product

NORTH, EAST, SOUTH, WEST = range(4)

# There is 8 variations per tile: all rotations + all rotations hflip

class Tile:

    def __init__(self, idx, body):
        body = np.array([list(map(int, l)) for l in body])
        self._image = body.copy()
        self._borders = {}
        for rot, hflip in product(range(4), range(2)):
            transformed = np.rot90(body, k=rot)
            if hflip:
                transformed = transformed[::-1]
            for direction in range(4):
                if direction == NORTH:
                    border = transformed[0]
                elif direction == SOUTH:
                    border = transformed[-1]
                elif direction == EAST:
                    border = transformed[:, -1]
                elif direction == WEST:
                    border = transformed[:, 0]
                border = int(''.join(map(str, border.tolist())), 2)
                self._borders[(direction, rot, hflip)] = border
        self.idx = idx
        self.hflip, self.rotation = 0, 0


    def get_border(self, direction):
        return self._borders[(direction, self.rotation, self.hflip)]

    def get_image(self):
        image = np.rot90(self._image, k=self.rotation)
        if self.hflip:
            image = image[::-1]
        return image[1:-1, 1:-1] # Borders are not part of the actual image

    def __repr__(self):
        return f'{self.idx} F{self.hflip}R{self.rotation}'

with open('input20.txt') as f:
    tiles = set()
    for tile in map(lambda x: x.splitlines(), f.read().replace('#', '1').replace('.', '0').split('\n\n')):
        header, body = tile[0], tile[1:]
        idx = int(header.replace('Tile ', '').replace(':', ''))
        tiles.add(Tile(idx, body))

# Brute & backtrack force all combinations?
S = int(np.sqrt(len(tiles)))

def backtrack(grid, pos, remaining_tiles):
    if pos == len(tiles):
        return True
    x = pos // S
    y = pos % S
    for tile in remaining_tiles:
        new_remaining_tiles = remaining_tiles.copy()
        new_remaining_tiles.remove(tile)
        for rotation, hflip in product(range(4), range(2)):
            tile.rotation = rotation
            tile.hflip = hflip
            grid[x][y] = tile
            # Check validity
            valid = True
            if x > 0:
                valid &= grid[x - 1][y].get_border(SOUTH) == tile.get_border(NORTH)
            if y > 0:
                valid &= grid[x][y - 1].get_border(EAST) == tile.get_border(WEST)
            if valid:
                if backtrack(grid, pos + 1, new_remaining_tiles):
                    return True
    return False

grid = [[None for _ in range(S)] for _ in range(S)]
result = backtrack(grid, 0, tiles.copy())
print(result)
value = grid[0][0].idx * grid[0][-1].idx * grid[-1][0].idx * grid[-1][-1].idx
print(value)

# Assemble the correct grid
image = -np.ones((8 * S, 8 * S))
for i, line in enumerate(grid):
    for j, tile in enumerate(line):
        image[8 * i : 8 * i + 8, 8 * j : 8 * j + 8] = tile.get_image()

# Scan the image for sea monsters
sea_monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
sea_monster = np.array([[int(c) for c in line] for line in sea_monster.replace('#', '1').replace(' ', '0').splitlines()])

for rot in range(4):
    for hflip in range(2):
        rotated = np.rot90(image, k=rot)
        if hflip:
            rotated = rotated[::-1]
        
        is_sea_monster = np.zeros_like(rotated)
        # Look for the sea monster in this rotated image
        for x in range(0, image.shape[0] - sea_monster.shape[0]):
            for y in range(0, image.shape[1] - sea_monster.shape[1]):
                if ((rotated[x : x + sea_monster.shape[0], y : y + sea_monster.shape[1]] * sea_monster) == sea_monster).all():
                    is_sea_monster[x : x + sea_monster.shape[0], y : y + sea_monster.shape[1]] += sea_monster

        is_sea_monster = np.abs(is_sea_monster)
        if is_sea_monster.sum():
            print((rotated * (1 - is_sea_monster)).sum())

