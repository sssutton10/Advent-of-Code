from collections import defaultdict

# Part 1
ws = open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/2024/Input_Day04.txt', 'r').readlines()
grid = defaultdict(str)

for i, x in enumerate(ws):
    for j, y in enumerate(x):
        grid[complex(i, j)] = y

dirs = [1, 1j, -1, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
xmas_count = 0

for i in range(len(ws)):
    for j in range(len(ws[0])):
        if grid[complex(i, j)] == 'X':
            for d in dirs:
                if grid[complex(i, j) + d] == 'M' and grid[complex(i, j) + 2*d] == 'A' and grid[complex(i, j) + 3*d] == 'S':
                    xmas_count += 1
print(xmas_count)

# Part 2
xmas_count = 0
dirs = [1+1j, 1-1j, -1+1j, -1-1j]

for i in range(len(ws)):
    for j in range(len(ws[0])):
        if grid[complex(i, j)] == 'M':
            for d in dirs:
                if grid[complex(i, j) + d] == 'A' and grid[complex(i, j) + 2*d] == 'S':
                    if grid[complex(i, j) + 2*d.real] == 'M' and grid[complex(i, j) + complex(0, 2*d.imag)] == 'S':
                        xmas_count += 1

                    if grid[complex(i, j) + 2*d.real] == 'S' and grid[complex(i, j) + complex(0, 2*d.imag)] == 'M':
                        xmas_count += 1

print(xmas_count / 2)