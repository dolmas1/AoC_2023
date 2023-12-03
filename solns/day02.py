#!/usr/bin/env python

import re

filename = "inputs/day02.txt"
#filename = "inputs/day02_sample.txt"

with open(filename) as f:
    input = f.read().splitlines()

def parse_line(x):
    
    id = x.split(':')[0]
    id = int(re.search('\d+', x)[0])

    
    game_info = x.split(':')[1].split(';')
    
    red, blue, green = 0, 0, 0
    
    for y in game_info:

        shown_reds = re.search('(\d+) red', y)
        shown_blues = re.search('(\d+) blue', y)
        shown_greens = re.search('(\d+) green', y)
        
        if shown_reds:
            red = max(red, int(shown_reds[1]))
        if shown_blues:
            blue = max(blue, int(shown_blues[1]))
        if shown_greens:
            green = max(green, int(shown_greens[1]))

    return {'id': id, 'red': red, 'blue': blue, 'green': green}


def is_possible(parsed_line):
    
    if parsed_line['red'] <= 12 and parsed_line['green'] <= 13 and parsed_line['blue'] <= 14:
        return True
    else:
        return False

def power(parsed_line):
    
    return parsed_line['red'] * parsed_line['blue'] * parsed_line['green']

def solve(input):
    
    ans_1, ans_2 = 0, 0

    for l in input:
        parsed = parse_line(l)
        
        if is_possible(parsed):
            ans_1 += parsed['id']

        ans_2 += power(parsed)
            
    return ans_1, ans_2

ans_1, ans_2 = solve(input)

print(ans_1)
print(ans_2)