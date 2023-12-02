#!/usr/bin/env python

import pandas as pd
import numpy as np
import re

f = open("inputs/01.txt", "r")
#f = open("inputs/01_sample.txt", "r")
#f = open("inputs/01_sample2.txt", "r")
input = f.readlines()

def solve_pt1(input):
    
    nums = [re.findall('\d', l) for l in input]

    nums_first_last = [int(x[0] + x[-1]) for x in nums]
    return sum(nums_first_last)

mapping = {'one': '1',
           'two': '2',
           'three': '3',
           'four': '4',
           'five': '5',
           'six': '6',
           'seven': '7',
           'eight': '8',
           'nine': '9'}

def match_number(s, mapping, rev = True):
    
    dig_match = re.match('\d', s)
    if dig_match:
        return dig_match[0]

    if rev == True:
        mapping_rev = {key[::-1]: val for key, val in mapping.items()}
    else:
        mapping_rev = mapping
                
    for key, val in mapping_rev.items():
            if s[:len(key)] == key:
                return val

    else:
        return None


def find_first(line, mapping):
    i = 0
    while i <= len(line):
        num = match_number(line[i:i+5], mapping, rev = False)
        if num:
            return num
        i += 1
    return



def find_last(line, mapping):
    i = 0
    while i <= len(line):
        num = match_number(line[::-1][i:i+5], mapping, rev = True)
        if num:
            return num
        i += 1
    return

def solve_pt2(input, mapping):

    ans_2 = 0
    
    for l in input:
        ans_2 += int(find_first(l, mapping) + find_last(l, mapping))
        
    return ans_2

print(solve_pt1(input), solve_pt2(input, mapping))