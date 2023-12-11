#!/usr/bin/env python
import numpy as np # TODO: do this without numpy (then update dockerfile back to alpine)

sample = 0

if sample == True:
    filename = "inputs/day11_sample.txt"
else:
    filename = "inputs/day11.txt"

with open(filename) as f:
    input = f.read().splitlines()

def parse(input):
    grid = np.zeros((len(input), len(input[0])))
    galaxies = []
    for i, l in enumerate(input):
        for j, c in enumerate(l):
            if c=='#':
                grid[i,j] = 1
                galaxies.append((i,j))
    return grid, galaxies

def solve(input):

    grid, galaxies = parse(input)

    rows_to_insert = np.where(grid.max(axis=1) == 0)[0]
    cols_to_insert = np.where(grid.max(axis=0) == 0)[0]
    
    ans_1 = 0
    ans_2 = 0
    for k, (i_1, j_1) in enumerate(galaxies):
        for l, (i_2, j_2) in enumerate(galaxies[:k]):
            x_dist = abs(i_2 - i_1)
            y_dist = abs(j_2 - j_1)
            extra_rows = ((rows_to_insert >= min(i_1, i_2)) & (rows_to_insert <= max(i_1, i_2))).sum()
            extra_cols = ((cols_to_insert >= min(j_1, j_2)) & (cols_to_insert <= max(j_1, j_2))).sum()
    
            
            dist = x_dist + y_dist + extra_rows + extra_cols
            dist2 = x_dist + y_dist + 999999*(extra_rows + extra_cols)
            ans_1 += dist
            ans_2 += dist2
    

    
    return ans_1, ans_2

ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)