#!/usr/bin/env python
import math

sample = 0

if sample == True:
    filename = "inputs/day06_sample.txt"
else:
    filename = "inputs/day06.txt"

with open(filename) as f:
    input = f.read().splitlines()


def parse_pt1(input):
    times = [int(x) for x in input[0][5:].split()]
    goals = [int(x) for x in input[1][9:].split()]
    return times, goals

def parse_pt2(input):
    time = int(input[0][5:].replace(' ', ''))
    goal = int(input[1][9:].replace(' ', ''))
    return time, goal

def solve(input):
    times, goals = parse_pt1(input)

    ans_1 = 1
    for time, goal in zip(times, goals):
        choices = [i for i in range(1,time)]
        distance = [c * (time - c) for c in choices]
        count_beaten = sum([a > goal for a in distance])
        ans_1 *= count_beaten

    time, goal = parse_pt2(input)

    # naive method for Pt2
    #choices = [i for i in range(1,time)]
    #distance = [c * (time - c) for c in choices]
    #count_beaten = sum([a > goal for a in distance])
    #ans_2 = count_beaten

    # use quadratic formula instead
    first_beaten = math.floor((float((-1*time)) - float((time ** 2 - (4 *goal)))** 0.5) / (-2))
    ans_2 = 1 + 2 * first_beaten - time
    
    return ans_1, ans_2

ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)