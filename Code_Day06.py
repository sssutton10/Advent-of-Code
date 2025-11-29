from collections import defaultdict
import re

coords = [[int(x) for x in re.findall('[0-9]+', y.strip())] for y in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2018/Inputs/Input_Day06.txt', 'r').readlines()]
coords = [complex(x, y) for x, y in coords]

# Part 1 and 2
grid_max = 360

check_coords = set(coords)
num_coords = defaultdict(int)
p2 = 0

for i in range(grid_max + 1):
    for j in range(grid_max + 1):
        dists = {}
        for coord in coords:
            dist = abs(coord.real - i) + abs(coord.imag - j)
            dists[coord] = dist
        min_dist = min(dists.values())
        closest = [k for k, v in dists.items() if v == min_dist]
        if len(closest) == 1:
            if i == 0 or i == grid_max or j == 0 or j == grid_max:
                check_coords.discard(closest[0])
            elif closest[0] in check_coords:
                num_coords[closest[0]] += 1
        
        if sum(dists.values()) < 10000:
            p2 += 1
            
print(max(num_coords.values()))
print(p2)
