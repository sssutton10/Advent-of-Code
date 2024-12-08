from collections import defaultdict

inp = open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day08.txt', 'r').readlines()

grid = defaultdict(str)
freqs = defaultdict(list)

for i, x in enumerate(inp):
    for j, y in enumerate(x.strip()):
        grid[complex(i, j)] = y
        if y != '.':
            freqs[y].append(complex(i, j))

p1 = set()
p2 = set()
for k, v in freqs.items():
    while len(v) > 1:
        curr_node = v.pop(0)
        p2.add(curr_node)
        for next_node in v:
            diff = next_node - curr_node
            if grid[next_node + diff] != '':
                p1.add(next_node + diff)
            if grid[curr_node - diff] != '':
                p1.add(curr_node - diff)
            
            i = 1
            while True:
                if grid[next_node + diff*i] == '':
                    break
                p2.add(next_node + diff*i)
                i += 1
            i = 1
            while True:
                if grid[curr_node - diff*i] == '':
                    break
                p2.add(curr_node - diff*i)
                i += 1
    p2.add(v[0])
            
print(len(p1))
print(len(p2))

# need 394 and 1277
