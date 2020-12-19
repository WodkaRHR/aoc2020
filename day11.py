import numpy as np

FLOOR = 0
EMPTY = 1
OCCUPIED = 2


with open('input11.txt') as f:
    grid = np.array([[{'.' : FLOOR, 'L' : EMPTY, '#' : OCCUPIED}[c] for c in line] for line in f.read().splitlines()])

def iterate_grid(grid):
    grid_new = grid.copy()
    for (i, j), _ in np.ndenumerate(grid):
        window = grid[np.maximum(0, i - 1) : i + 2, np.maximum(0, j - 1) : j + 2]
        if grid[i, j] == EMPTY:
            if (window == OCCUPIED).sum() == 0:
                grid_new[i, j] = OCCUPIED
        elif grid[i, j] == OCCUPIED:
            if (window == OCCUPIED).sum() - 1 >= 4:
                grid_new[i, j] = EMPTY
    return grid_new

def iterate_grid2(grid):
    grid_new = grid.copy()
    for (i, j), seat in np.ndenumerate(grid):
        if seat == FLOOR:
            continue
        num_occupied_visible = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di != 0 or dj != 0:
                    # Ray-search
                    ii, jj = i + di, j + dj
                    while ii in range(grid.shape[0]) and jj in range(grid.shape[1]):
                        if grid[ii, jj] == EMPTY:
                            #print('For', i, j, 'dir', di, dj, 'visible empty')
                            break
                        if grid[ii, jj] == OCCUPIED:
                            #print('For', i, j, 'dir', di, dj, 'visible occ')
                            num_occupied_visible += 1
                            break
                        ii += di
                        jj += dj
        if seat == OCCUPIED and num_occupied_visible >= 5:
            grid_new[i, j] = EMPTY
        elif seat == EMPTY and num_occupied_visible == 0:
            grid_new[i, j] = OCCUPIED
    return grid_new

while True:
    grid_new = iterate_grid2(grid)
    if (grid == grid_new).all():
        print((grid_new == OCCUPIED).sum())
        break
    else:
        grid = grid_new
