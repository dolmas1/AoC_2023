#!/usr/bin/env python
import re

sample = 0

if sample == True:
    filename = "inputs/day07_sample.txt"
else:
    filename = "inputs/day07.txt"

with open(filename) as f:
    input = f.read().splitlines()

def parse_pt1(input):
    hands = []
    bids = []
    for l in input:
        hand, bid = l.split()
        hands.append(hand)
        bids.append(int(bid))

    return hands, bids

def hand_type(hand):
    
    counts = []
    for c in set(hand):
        counts.append(hand.count(c))
    counts.sort(reverse = True)
    
    if counts[0] == 5:
        hand_type = '1' # five kind
    elif counts[0] == 4:
        hand_type = '2' # four kind
    elif counts[0] == 3 and counts[1] == 2:
        hand_type = '3' # full house
    elif counts[0] == 3:
        hand_type = '4' # three kind
    elif counts[1] == 2:
        hand_type = '5' # two pair
    elif counts[0] == 2:
        hand_type = '6' # pair
    else:
        hand_type = '7' # high card
    
    return hand_type


def improve_hand(hand):
    if 'J' in hand:
        if hand == 'JJJJJ':
            return 'AAAAA'
        else:
            rest_of_hand = [c for c in hand if c != 'J']
            best_replacement = max(set(rest_of_hand), key=rest_of_hand.count)
            return re.sub(r'J', best_replacement, hand)
    else:
        return hand


def solve(input):
    hands, bids = parse_pt1(input)

    rank_single_map_pt1 = {'A':'01',
        'K':'02',
        'Q':'03',
        'J':'04',
        'T':'05',
        '9':'06',
        '8':'07',
        '7':'08',
        '6':'09',
        '5':'10',
        '4':'11',
        '3':'12',
        '2':'13'}
    
    hand_ranks = [hand_type(h) + ''.join([rank_single_map_pt1[c] for c in h]) for h in hands]

    hand_ranks, hands, bids = (list(t) for t in zip(*sorted(zip(hand_ranks, hands, bids), reverse=True)))

    ans_1 = sum([bid * (i + 1) for i, bid in enumerate(bids)])

    rank_single_map_pt2 = {'A':'01',
        'K':'02',
        'Q':'03',
        'J':'14',
        'T':'05',
        '9':'06',
        '8':'07',
        '7':'08',
        '6':'09',
        '5':'10',
        '4':'11',
        '3':'12',
        '2':'13'}
    
    hand_ranks = [hand_type(improve_hand(h)) + ''.join([rank_single_map_pt2[c] for c in h]) for h in hands]

    hand_ranks, hands, bids = (list(t) for t in zip(*sorted(zip(hand_ranks, hands, bids), reverse=True)))

    ans_2 = sum([bid * (i + 1) for i, bid in enumerate(bids)])
    
    return ans_1, ans_2



ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)