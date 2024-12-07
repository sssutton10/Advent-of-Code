from collections import defaultdict

inp = [x.strip() for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day06.txt', 'r').readlines()]
patrol = defaultdict(str)

for i, x in enumerate(inp):
    for j, y in enumerate(x):
        patrol[complex(i, j)] = y
        if y == '^':
            current_pos = complex(i, j)

# Part 1
d = complex(-1, 0)
visited = set([current_pos])
visited_p2 = set()

while True:
    new_pos = current_pos + d
    if patrol[new_pos] == '':
        break
    if patrol[new_pos] == '#':
        d *= -1j
        new_pos = current_pos + d
    visited.add(new_pos)
   
    if new_pos not in [x[0] for x in visited_p2]:
        visited_p2.add((new_pos, d))
    current_pos = new_pos
print(len(visited))

# Part 2
p2 = 0

for loc, d in visited_p2:
    grid = patrol.copy()
    grid[loc] = '#'
    current_pos = loc - d
    visited_temp = set([(current_pos, d)])
   
    while True:
        new_pos = current_pos + d
        if (new_pos, d) in visited_temp:
            p2 += 1
            break
        visited_temp.add((new_pos, d))
        if grid[new_pos] == '':
            break
        if grid[new_pos] == '#':
            d *= -1j
            new_pos = current_pos
            # new_pos = current_pos + d
            # if grid[new_pos] != '#':
            #     break
        # visited_temp.add((new_pos, d))
        current_pos = new_pos
print(p2)