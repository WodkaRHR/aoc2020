import numpy as np
import scipy.ndimage

input = """.#.##..#
....#.##
##.###..
.#.#.###
#.#.....
.#..###.
.#####.#
#..####.""".splitlines()
initial_slice = np.array([
    [1 if c == '#' else 0 for c in line] for line in input
], dtype=np.int)
initial_slice = np.expand_dims(initial_slice, -1)

n_cycles = 6

h, w, d = initial_slice.shape
cube = np.zeros((h + 2 * n_cycles, w + 2 * n_cycles, d + 2 * n_cycles))
cube[n_cycles : n_cycles + h, n_cycles : n_cycles + w, n_cycles : n_cycles + d] = initial_slice

filter = np.ones((3, 3, 3), dtype=np.int)
filter[1, 1, 1] = 0

for _ in range(n_cycles):
    num_active_neighbours = scipy.ndimage.convolve(cube, filter, mode='constant', cval=0)
    remaining_active = cube * (num_active_neighbours >= 2) * (num_active_neighbours <= 3)
    new_active = (1 - cube) * (num_active_neighbours == 3)
    cube = remaining_active + new_active

print(cube.sum())

h, w, d = initial_slice.shape
cube = np.zeros((h + 2 * n_cycles, w + 2 * n_cycles, d + 2 * n_cycles))
cube[n_cycles : n_cycles + h, n_cycles : n_cycles + w, n_cycles : n_cycles + d] = initial_slice

# Part 2
initial_slice = np.expand_dims(initial_slice, -1)
h, w, d, e = initial_slice.shape
cube = np.zeros((h + 2 * n_cycles, w + 2 * n_cycles, d + 2 * n_cycles, e + 2 * n_cycles))
cube[n_cycles : n_cycles + h, n_cycles : n_cycles + w, n_cycles : n_cycles + d, n_cycles : n_cycles + e] = initial_slice

filter = np.ones((3, 3, 3, 3), dtype=np.int)
filter[1, 1, 1, 1] = 0

for _ in range(n_cycles):
    num_active_neighbours = scipy.ndimage.convolve(cube, filter, mode='constant', cval=0)
    remaining_active = cube * (num_active_neighbours >= 2) * (num_active_neighbours <= 3)
    new_active = (1 - cube) * (num_active_neighbours == 3)
    cube = remaining_active + new_active

print(cube.sum())