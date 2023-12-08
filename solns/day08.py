#!/usr/bin/env python
import math

sample = 0

if sample == True:
    filename = "inputs/day08_sample.txt"
else:
    filename = "inputs/day08.txt"

with open(filename) as f:
    input = f.read().splitlines()


def parse(input):
    instructions = [x for x in input[0]]
    nodes = {}
    for l in input[2:]:
        key, vals = l.split(' = ')
        left, right = vals[1:-1].split(', ')
        nodes[key] = {'L': left, 'R': right}
    return instructions, nodes


def solve(input):

    instructions, nodes = parse(input)

    # pt1
    current_loc = 'AAA'
    i = 0
    while not current_loc == 'ZZZ':
        current_loc = nodes[current_loc][instructions[i % len(instructions)]]
        i += 1

    ans_1 = i

    # pt2
    ans = []
    starting_locs = [n for n in nodes.keys() if n[-1] == 'A']
    for current_loc in starting_locs:
        i = 0
        while not current_loc[-1] == 'Z':
            current_loc = nodes[current_loc][instructions[i % len(instructions)]]
            i += 1
        ans.append(i)
    
    ans_2 = math.lcm(*ans)
    
    return ans_1, ans_2


ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)