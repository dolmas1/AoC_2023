#!/usr/bin/env python
sample = 0

if sample == True:
    filename = "inputs/day04_sample.txt"
else:
    filename = "inputs/day04.txt"

with open(filename) as f:
    input = f.read().splitlines()

def parse_input(input):
    cards = {}
    for i, l in enumerate(input):
        winning, ours = [set(x.strip().split()) for x in l.split(':')[1].split('|')]
        intersect = winning.intersection(ours)
        cards[i] = {'num_held': 1, 'winning_numbers': len(intersect)}
    return(cards)

def solve(input):
    cards = parse_input(input)
    ans_1 = sum([2**(x['winning_numbers']-1) for x in cards.values() if x['winning_numbers'] > 0])

    for key, val in cards.items():
        for i in range(val['winning_numbers']):
            cards[key + i + 1]['num_held'] += (val['num_held'])

    ans_2 = sum([x['num_held'] for x in cards.values()])
    
    return ans_1, ans_2

ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)