import numpy as np
from collections import defaultdict
from itertools import product

NORTH, EAST, SOUTH, WEST = range(4)

class Tile:

    def __init__(self, idx, body):
        body = np.array([list(map(int, l)) for l in body])
        self._borders = {}
        self._border_to_orientation = defaultdict(set)
        for rot, hflip, vflip in product(range(4), range(2), range(2)):
            transformed = np.rot90(body, k=rot)
            if hflip:
                transformed = transformed[::-1]
            if vflip:
                transformed = transformed[:, ::-1]
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
                self._borders[(direction, rot, hflip, vflip)] = border
                self._border_to_orientation[border].add((direction, rot, hflip, vflip))
        self.idx = idx
        self.hflip, self.vflip, self.rotation = 0, 0, 0


    def get_border(self, direction):
        return self._borders[(direction, self.rotation, self.hflip, self.vflip)]

    def __repr__(self):
        return f'{self.idx} F{self.hflip}{self.vflip}{self.rotation}'


with open('input20.txt') as f:
    tiles = set()
    for tile in map(lambda x: x.splitlines(), f.read().replace('#', '1').replace('.', '0').split('\n\n')):
        header, body = tile[0], tile[1:]
        idx = int(header.replace('Tile ', '').replace(':', ''))
        tiles.add(Tile(idx, body))


# Brute & backtrack force all combinations?
S = int(np.sqrt(len(tiles)))




def brute_force(grid, pos, remaining_tiles):
    if pos == len(tiles):
        return True
    x = pos // S
    y = pos % S
    for tile in remaining_tiles:
        new_remaining_tiles = remaining_tiles.copy()
        new_remaining_tiles.remove(tile)
        for rotation, hflip, vflip in product(range(4), range(2), range(2)):
            tile.rotation = rotation
            tile.hflip = hflip
            tile.vflip = vflip
            grid[x][y] = tile
            # Check validity
            valid = True
            if x > 0:
                valid &= grid[x - 1][y].get_border(SOUTH) == tile.get_border(NORTH)
            if y > 0:
                valid &= grid[x][y - 1].get_border(EAST) == tile.get_border(WEST)
            if valid:
                if brute_force(grid, pos + 1, new_remaining_tiles):
                    return True
    return False

grid = [[None for _ in range(S)] for _ in range(S)]
result = brute_force(grid, 0, tiles.copy())
print(result)
value = grid[0][0].idx * grid[0][-1].idx * grid[-1][0].idx * grid[-1][-1].idx
print(value)