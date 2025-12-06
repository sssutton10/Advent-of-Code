import time
start_time = time.time()

import math

inp = [x.strip() for x in open('2025/Inputs/Input_Day06.txt', 'r').readlines()]
ops = inp[-1].split()
vals = [[int(y) for y in x.split()] for x in inp[:-1]]

# Part 1
p1 = 0
for i, op in enumerate(ops):
    if op == '+':
        p1 += sum([y[i] for y in vals])
    else:
        p1 += math.prod([y[i] for y in vals])
print(p1)

# Part 2
inp_p2 = [x.strip('\n') for x in open('2025/Inputs/Input_Day06.txt', 'r').readlines()][:-1]
p2 = 0
curr_ind = end_ind = 0
for i, op in enumerate(ops):
    for v in inp_p2:
        end_ind = max(end_ind, v[curr_ind:].find(' ') + curr_ind)
    if end_ind == (len(v) - 1) or end_ind < curr_ind:
        end_ind = len(v)
    nums = []
    for j in reversed(range(curr_ind, end_ind)):
        nums.append(int(''.join(v[j] for v in inp_p2)))
    p2 += sum(nums) if op == '+' else math.prod(nums)
    curr_ind = end_ind + 1
print(p2)

end_time = time.time()
print(f"{end_time - start_time:.4f}")