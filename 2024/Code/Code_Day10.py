from collections import defaultdict

trail_map = defaultdict(lambda: -1)
trail_heads = {}

inp = [
    x.strip()
    for x in open(
        "C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day10.txt", "r"
    ).readlines()
]

for i, x in enumerate(inp):
    for j, y in enumerate(x):
        trail_map[complex(i, j)] = int(y)
        if int(y) == 0:
            trail_heads[complex(i, j)] = set()
            
trail_heads_p2 = {th: 0 for th in trail_heads}

dirs = [1, -1, 1j, -1j]
p1 = 0

for th in trail_heads:
    next_locs = [(th + d, 0) for d in dirs]

    while len(next_locs) > 0:
        next_loc, val = next_locs.pop()

        if val == 8 and trail_map[next_loc] == 9:
            trail_heads[th].add(next_loc)
            trail_heads_p2[th] += 1
        else:
            if (trail_map[next_loc] - 1) == val:
                for d in dirs:
                    next_locs.append((next_loc + d, val + 1))

print(sum([len(x) for x in trail_heads.values()]))
print(sum([x for x in trail_heads_p2.values()]))