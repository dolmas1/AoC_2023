#!/usr/bin/env python
import re

filename = "inputs/day03.txt"
#filename = "inputs/day03_sample.txt"

with open(filename) as f:
    input = f.read().splitlines()

def check_neighbourhood(input, span, n = 1):
    '''
    Check whether a given number is a part number

            Parameters:
                    input (list): input grid (list of strings)
                    span (list): [[0,1], [0,3]] if number being checked starts in row 0, col 1, and ends in row 0, col 3
                    n (int): how many positions (in any direction) far away count as 'adjacent'

            Returns:
                    bool: whether a character was found in the vicinity of the number
    '''

    start_i = span[0][0]
    start_j = span[0][1]
    end_i = span[1][0]
    end_j = span[1][1]

    # determine the boundaries of neighbourhood to search:
    neighbourhood_min_i = max(0, start_i - n)
    neighbourhood_max_i = min(len(input)-1, end_i + n)
    neighbourhood_min_j = max(0, start_j - n)
    neighbourhood_max_j = min(len(input[0])-1, end_j + n)
    
    # search until you find a symbol:
    for i in range(neighbourhood_min_i, neighbourhood_max_i+1):
        for j in range(neighbourhood_min_j, neighbourhood_max_j+1):
            if re.match('[^\d\.]', input[i][j]): 
                return True

    return False


def find_numbers(input):
    "Find all numbers, along with their respecitive location/spans"
    nums = []
    num_spans = []
    
    for i, l in enumerate(input):
        for match in re.finditer(r'(\d+)', l):
            nums.append(int(match.group()))
            num_spans.append([[i, match.span()[0]], [i, match.span()[1]-1]])

    return nums, num_spans


def find_potential_gears(input):
    "Returns the [i,j] locations of all * characters"
    potential_gears = []
    for i, l in enumerate(input):
            for match in re.finditer(r'(\*)', l):

                potential_gears.append([i, match.span()[0]])
    return potential_gears


def is_adjacent(potential_gear, num_span):
    "given a potential gear [i, j], check against num_span [[i,j], [i,j]] and return whether num_span is adjacent to gear"

    min_i = min(num_span[0][0]-1, num_span[1][0]-1)
    max_i = max(num_span[0][0]+1, num_span[1][0]+1)
    min_j = min(num_span[0][1]-1, num_span[1][1]-1)
    max_j = max(num_span[0][1]+1, num_span[1][1]+1)

    if potential_gear[0] >= min_i and potential_gear[0] <= max_i and potential_gear[1] >= min_j and potential_gear[1] <= max_j:
        return True

    else:
        return False


def find_gear_ratio(potential_gear, nums, num_spans):
    "given a potential gear [i, j], check against nums and num_spans to calculate gear ratio (if applicable)"
    nearby_nums = [num for num, span in zip(nums, num_spans) if is_adjacent(potential_gear, span)]
    if len(nearby_nums) == 2:
        return nearby_nums[0] * nearby_nums[1]
    else:
        return 0


def solve(input):
    
    nums, num_spans = find_numbers(input)

    # pt 1
    ans_1 = 0

    for num, span in zip(nums, num_spans):
        if check_neighbourhood(input, span, n = 1):
            ans_1 += num

    # pt 2
    ans_2 = 0

    potential_gears = find_potential_gears(input)
    
    for potential_gear in potential_gears:
        ans_2 += find_gear_ratio(potential_gear, nums, num_spans)


    return ans_1, ans_2

ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)