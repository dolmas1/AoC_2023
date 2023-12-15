#!/usr/bin/env python
from collections import defaultdict 

sample = 0

if sample == True:
    filename = "inputs/day15_sample.txt"
else:
    filename = "inputs/day15.txt"

with open(filename) as f:
    input = f.read()#.splitlines()

def parse_pt2(s):
    if s[-2] == '=':
        return s[:-2], int(s[-1])
    else:
        return s[:-1], 0

def parse(input):
    parsed_pt1 = input.split(',')
    parsed_pt2 = [parse_pt2(s) for s in parsed]
    return parsed_pt1, parsed_pt2

def HASH(str_input):
    current_val = 0
    for c in str_input:
        current_val += ord(c)
        current_val *= 17
        current_val = current_val % 256
    return current_val

def def_value(): 
    return ([], [])

def add_lens(label, f, boxes):
    labels, focals = boxes[HASH(label)]

    try:
        idx = labels.index(label)
        focals[idx] = f
    except:
        labels.append(label)
        focals.append(f)

    boxes[HASH(label)] = labels, focals

def remove_lens(label, boxes):
    labels, focals = boxes[HASH(label)]

    try:
        idx = labels.index(label)
        del labels[idx]
        del focals[idx]
    except:
        pass

    boxes[HASH(label)] = labels, focals

def solve(input):
    parsed_pt1, parsed_pt2  = parse(input)
    ans_1 = 0
    for str_input in parsed_pt1:
        ans_1 += HASH(str_input)
        
    ans_2 = 0
    boxes = defaultdict(def_value)

    for label, f in parsed_pt2:
        if f > 0:
            add_lens(label, f, boxes)
        else:
            remove_lens(label, boxes)

    for key, val in boxes.items():
        for i, v in enumerate(val[1]):
            ans_2 += (key + 1) * (i+1) * (v)
    
    return ans_1, ans_2

ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)