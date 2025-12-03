inp = [int(x[1:]) * (1 if x[0] == 'R' else -1) for x in open('./Input_Day01.txt', 'r').readlines()]

# Part 1
curr_pos = 50
count_zero = 0

for i in inp:
    curr_pos = (curr_pos + i) % 100
    if curr_pos == 0:
        count_zero += 1
print(count_zero)

# Part 2
curr_pos = 50
count_zero = 0

for i in inp:
    new_pos = curr_pos + i
    if new_pos >= 100 :
        count_zero += abs(new_pos // 100)
    elif new_pos <= 0:
        count_zero += ((100 - curr_pos) + abs(i)) // 100
        if curr_pos == 0:
            count_zero -= 1
    curr_pos = new_pos % 100
print(count_zero)
