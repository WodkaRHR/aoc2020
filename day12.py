
import numpy as np

with open('input12.txt') as f:
    lines = f.read().splitlines()

EAST, SOUTH, WEST, NORTH = range(4)
d = np.array([
    [1, 0],
    [0, -1],
    [-1, 0],
    [0, 1],
], dtype=np.int)

char_to_dir = {
    'N' : NORTH,
    'S' : SOUTH,
    'W' : WEST,
    'E' : EAST,
}

pos = np.zeros(2, dtype=np.int)
heading = EAST
for line in lines:
    c, n = line[:1], int(line[1:])
    if c == 'L':
        heading = (heading - n // 90) % 4
    elif c == 'R':
        heading = (heading + n // 90) % 4
    elif c == 'F':
        pos += n * d[heading]
    else:
        pos += n * d[char_to_dir[c]]

print(np.sum(np.abs(pos)))
        
pos_ship = np.zeros(2, dtype=np.int)
pos_wp = np.array([10, 1], dtype=np.int)
R = np.array([
    [0, -1],
    [1, 0],
])
for line in lines:
    c, n = line[:1], int(line[1:])
    if c == 'F':
        pos_ship += n * pos_wp
    elif c == 'R':
        p = (-n // 90) % 4
        pos_wp = np.linalg.matrix_power(R, p) @ pos_wp
    elif c == 'L':
        p = (n // 90) % 4
        pos_wp = np.linalg.matrix_power(R, p) @ pos_wp
    else:
        pos_wp += n * d[char_to_dir[c]]
        
print(np.sum(np.abs(pos_ship)))


