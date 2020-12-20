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
        self._border_to_orientation = defaultdict(set)
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
                self._border_to_orientation[border].add((direction, rot, hflip))
        self.idx = idx
        self.hflip, self.rotation = 0, 0


    def get_border(self, direction):
        return self._borders[(direction, self.rotation, self.hflip)]

    def get_image(self):
        image = np.rot90(self._image, k=self.rotation)
        if self.hflip:
            image = image[::-1]
        return image

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

# Assemble the correct grid
image = -np.ones((10 * S, 10 * S))
for i, line in enumerate(grid):
    for j, tile in enumerate(line):
        image[10 * i : 10 * i + 10, 10 * j : 10 * j + 10] = tile.get_image()

print(image[:21, :21])