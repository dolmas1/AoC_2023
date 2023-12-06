#!/usr/bin/env python
sample = 0

if sample == True:
    filename = "inputs/day05_sample.txt"
else:
    filename = "inputs/day05.txt"

with open(filename) as f:
    input = f.read().splitlines()


def map_seed_pt1(seed, mapping):
    mapped_seed = seed
    for src, [dest, r] in mapping.items():
        diff = seed - src
        if diff >= 0 and diff < r:
            mapped_seed = dest + diff
            
    return mapped_seed


def map_seed_pt2(input_seeds, mapping):
    output_seeds = []

    # run until list of source seeds ranges is depleted
    while len(input_seeds) > 0:
        
        # check every seed range against every mapping source range:
        seed = input_seeds.pop()
        output_seeds.append(seed) # assume it passes straight through, we'll pop later if not
        for src, [dest, r] in mapping.items():
            
            # case when no overlap
            if seed[0] >= src + r or seed[1] < src:
                pass
    
            # when overlap
            else :
                left_overhang = (seed[0], min(src, seed[1])-1)
                right_overhang = (max(seed[0], src+r-1)+1, seed[1])
                intersection = (max(seed[0], src) + dest - src, min(seed[1], src+r-1) + dest - src)
                
                if left_overhang[0] <= left_overhang[1]:
                    input_seeds.append(left_overhang)
                if right_overhang[0] <= right_overhang[1]:
                    input_seeds.append(right_overhang)
    
                _ = output_seeds.pop()
                output_seeds.append(intersection)
    
                break

    # finally, cleanup any overlaps in the output_seed ranges:
    # TODO  (OPTIONAL BUT EFFICIENT?)
    
    return output_seeds


def solve(input):

    # parse the initial seeds
    seeds_pt1 = [int(a) for a in input[0][7:].split()] # for pt1

    seeds_pt2 = []
    for i in range(0, len(seeds_pt1), 2):
        seeds_pt2.append((seeds_pt1[i], seeds_pt1[i] + seeds_pt1[i+1] - 1))

    
    mapping = {}
    
    for i, l in enumerate(input[3:]):
        
        # process the current mapping (as we have finished reading it), then reset it
        if l == '':
            
            seeds_pt1 = [map_seed_pt1(seed, mapping) for seed in seeds_pt1]
            seeds_pt2 = map_seed_pt2(seeds_pt2, mapping)
            mapping = {}
            
        # append current row to the new mapping which is being built
        elif re.match('\d', l[0]):
            dest, src, r = [int(a) for a in l.split()]
            mapping[src] = [dest, r]
    
    # one final processing step (for the final mapping)
    seeds_pt1 = [map_seed_pt1(seed, mapping) for seed in seeds_pt1]
    seeds_pt2 = map_seed_pt2(seeds_pt2, mapping)

    ans_1 = min(seeds_pt1)

    ans_2 = min([seed[0] for seed in seeds_pt2])

    return ans_1, ans_2



ans_1, ans_2 = solve(input)
print(ans_1)
print(ans_2)