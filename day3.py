import numpy as np
import functools, operator

with open('input3.txt') as f:
    grid = np.array([[char == '#' for char in line] for line in f.read().splitlines()])

result = []
for dj, di in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    num_trees = 0
    j = 0
    for i in range(0, grid.shape[0], di):
        if grid[i, j % grid.shape[1]]:
            num_trees += 1
        j += dj
    result.append(num_trees)
print(result)
print(functools.reduce(operator.mul, result, 1))
