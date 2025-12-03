import re
from collections import defaultdict

claims = [re.findall('[0-9]+', y.strip()) for y in open('./Day_3.txt', 'r').readlines()]

# Part 1
counts = defaultdict(int)
for claim in claims:
    start_point = complex(int(claim[1]), int(claim[2]))
    for i in range(int(claim[3])):
        for j in range(int(claim[4])):
            counts[start_point + complex(i, j)] += 1
print(sum([1 for v in counts.values() if v > 1]))

# Part 2
for claim in claims:
    start_point = complex(int(claim[1]), int(claim[2]))
    if counts[start_point] > 1:
        continue
   
    overlap = False
    for i in range(int(claim[3])):
        for j in range(int(claim[4])):
            if counts[start_point + complex(i, j)] > 1:
                overlap = True
    if not overlap:
        print(claim[0])
        break