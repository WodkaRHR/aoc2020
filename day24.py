from collections import Counter
import numpy as np

E, SE, SW, W, NW, NE = map(str, range(6))

with open('input24.txt') as f:
    content = f.read()
    for char, sym in (('se', SE), ('sw', SW), ('nw', NW), ('ne', NE), ('e', E), ('w', W)): # The order is important here: 2-char keys before 1-char keys
        content = content.replace(char, sym)
    sequences = content.splitlines()

moves = {
    E : ((1, 0), (1, 0)),
    SE : ((1, 1), (0, 1)),
    SW : ((0, 1), (-1, 1)),
    W : ((-1, 0), (-1, 0)),
    NW : ((0, -1), (-1, -1)),
    NE : ((1, -1), (0, -1)),
}

def sequence_to_coords(sequence):
    x, y = 0, 0
    for move in sequence:
        dx, dy = moves[move][y % 2]
        x += dx
        y += dy
    return x, y

counts = Counter(sequence_to_coords(s) for s in sequences)
black_tiles = set(coords for coords in counts if counts[coords] % 2 == 1)
print(len(black_tiles))

# We only have to check black tiles and all tiles adjacent to black tiles
for day in range(100):
    tiles_to_check = set()
    for x, y in black_tiles:
        for move, delta in moves.items():
            dx, dy = delta[y % 2]
            tiles_to_check.add((x + dx, y + dy))
        tiles_to_check.add((x, y))

    next_black_tiles = set()
    for x, y in tiles_to_check:
        num_adj_black_tiles = 0
        for move, delta in moves.items():
            dx, dy = delta[y % 2]
            if (x + dx, y + dy) in black_tiles:
                num_adj_black_tiles += 1
        if (x, y) in black_tiles:
            if num_adj_black_tiles in (1, 2):
                next_black_tiles.add((x, y))
        else:
            if num_adj_black_tiles == 2:
                next_black_tiles.add((x, y))
    black_tiles = next_black_tiles

print(len(black_tiles))
            


