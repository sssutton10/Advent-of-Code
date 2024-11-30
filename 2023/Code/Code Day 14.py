rocks_init = list(open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2023/Inputs/Input Day 14.txt').read().split('\n'))
rocks = [[x[i] for x in rocks_init] for i in range(len(rocks_init[0]))]

def tilt_row(r):
    new_row = r
    next_open = 0 if new_row[0] == '.' else 1
    for i in range(1, len(new_row)):
        if new_row[i] == '.':
            continue
        elif new_row[i] == 'O':
            new_row[i] = '.'
            new_row[next_open] = 'O'
            next_open += 1
        else:
            next_open = i + 1
    return new_row

p1 = 0
for rock_col in rocks:
    new_row = tilt_row(rock_col)
    p1 += sum([len(new_row) - i if new_row[i] == 'O' else 0 for i in range(len(new_row))])

print(p1)

def tilt_row_rev(r):
    new_row = r
    next_open = 0 if new_row[0] == '.' else 1
    for i in reversed(range(1, len(new_row))):
        if new_row[i] == '.':
            continue
        elif new_row[i] == 'O':
            new_row[i] = '.'
            new_row[next_open] = 'O'
            next_open -= 1
        else:
            next_open = i - 1
    return new_row

for rock_col in rocks:
    new_row = til_row