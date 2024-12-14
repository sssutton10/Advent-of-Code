from collections import defaultdict

plants = defaultdict(str)
inp = [x.strip() for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day12.txt', 'r').readlines()]

for i, x in enumerate(inp):
    for j, y in enumerate(x):
        plants[complex(i, j)] = y

def find_bulk_perimeter(p, re):
    perimeter = 0
    included = set()
    curr_plant = p[re[0]]
    re = sorted(re, key=lambda x: (x.real, x.imag))
    for r in re:
        for f, d in [(-1j, 1), (1j, 1), (1, 1j), (-1, 1j)]:
            if p[r + f] != curr_plant and (r, f) not in included:
                new_r = r
                included.add((new_r, f))
                while True:
                    new_r += d
                    if p[new_r] != curr_plant or p[new_r + f] == curr_plant:
                        break

                    included.add((new_r, f))
                perimeter += 1
    return perimeter

seen = set()
dirs = [1, -1, 1j, -1j]
cost_p1 = 0
cost_p2 = 0

for i in range(len(inp)):
    for j in range(len(inp[0])):
        
        if complex(i, j) in seen:
            continue

        curr_plant = plants[complex(i, j)]
        region = [complex(i, j)]
        seen.add(complex(i, j))
        queue = [complex(i, j) + d for d in dirs if plants[complex(i, j) + d] == curr_plant]
        area = 1
        perimeter = sum([1 if plants[complex(i, j) + d] != curr_plant else 0 for d in dirs])

        while len(queue) > 0:
            next_loc = queue.pop()
            
            if next_loc in seen:
                continue

            seen.add(next_loc)
            region.append(next_loc)
            area += 1
            perimeter += sum([1 if plants[next_loc + d] != curr_plant else 0 for d in dirs])

            for d in dirs:
                if plants[next_loc + d] == curr_plant:
                    queue.append(next_loc + d)

        cost_p1 += area * perimeter
        cost_p2 += area * find_bulk_perimeter(plants, region)

print(cost_p1)
print(cost_p2)
