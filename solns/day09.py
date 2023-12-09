#!/usr/bin/env python
sample = 0

if sample == True:
    filename = "inputs/day09_sample.txt"
else:
    filename = "inputs/day09.txt"

with open(filename) as f:
    input = f.read().splitlines()

def parse(input):
    inputs = []
    for l in input:
        inputs.append([int(x) for x in l.split(' ')])

    return inputs

def get_diffs(line):
    diffs = [line[i+1] - v for i, v in enumerate(line[:-1])]
    if all(v == 0 for v in diffs):
        is_done = True
    else:
        is_done = False
    last_val = diffs[-1]
    return diffs, is_done, last_val

def solve_line(line):
    is_done = False
    last_vals = []
    diffs = line
    while not is_done:
        diffs, is_done, last_val = get_diffs(diffs)
        last_vals.append(last_val)
    next_val = sum(last_vals) + line[-1]
    return next_val

def solve(input):
    inputs = parse(input)
    zips = list(zip(*[(solve_line(l), solve_line(l[::-1])) for l in inputs])) ## TODO: do properly rather than solve each direction separately
    ans_1 = sum(zips[0])
    ans_2 = sum(zips[1])
    return ans_1, ans_2

ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)