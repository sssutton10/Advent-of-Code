import functools

inp_raw = [x.strip() for x in open('2025/Inputs/Input_Day07.txt', 'r').readlines()]
grid = {}
for j, r in enumerate(inp_raw):
    for i, s in enumerate(r):
        grid[complex(i, j)] = s
        
        if s == 'S':
            start_pos = complex(i, j)
            
grid_p2 = grid.copy()

grid[start_pos + 1j] = '|'

split_count = 0
for j, r in enumerate(inp_raw[1:-1]):
    for i, s in enumerate(r):
        if grid[complex(i, j)] in ['.', '^']:
            continue
        if grid[complex(i, j) + 1j] == '.':
            grid[complex(i, j) + 1j] = '|'
        elif grid[complex(i, j) + 1j] == '^':
            split_count += 1
            grid[complex(i, j) + (-1 + 1j)] = '|'
            grid[complex(i, j) + (1 + 1j)] = '|'
print(split_count)

# Part 2
split_count = 0
curr_pos = start_pos + 1j
last_row = len(inp_raw) - 1

@functools.cache
def solve(pos):
    if pos.imag == last_row:
        return 1
    
    if grid_p2[pos + 1j] == '.':
        return solve(pos + 1j)
    elif grid_p2[pos + 1j] == '^':
        return (solve(pos + (-1 + 1j)) + solve(pos + (1 + 1j)))

print(solve(curr_pos))
