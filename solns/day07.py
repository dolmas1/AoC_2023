#!/usr/bin/env python
import math

sample = 0

if sample == True:
    filename = "inputs/day06_sample.txt"
else:
    filename = "inputs/day06.txt"

with open(filename) as f:
    input = f.read().splitlines()




def solve(input):
    times, goals = parse_pt1(input)


    
    return ans_1, ans_2

ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)