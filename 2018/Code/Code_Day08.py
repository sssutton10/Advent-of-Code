from collections import deque, defaultdict

inp = deque([int(x) for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2018/Inputs/Input_Day08.txt', 'r').read().split()])

# Part 1
inp_p1 = inp.copy()
children = inp_p1.popleft()
metadata = inp_p1.popleft()

def recurse(c, m, i, p1_sum = 0):
    if c == 0:
        for j in range(m):
            p1_sum += i.popleft()
        return (p1_sum, i)
    for j in range(c):
        new_c = i.popleft()
        new_m = i.popleft()
        p1_sum, i = recurse(new_c, new_m, i, p1_sum)
    
    for j in range(m):
            p1_sum += i.popleft()
    return (p1_sum, i)

p1_ans, _ = recurse(children, metadata, inp_p1, 0)
print(p1_ans)

# Part 2 - needed to look at solutions for this part
inp_p2 = inp.copy()
children = inp_p2.popleft()
metadata = inp_p2.popleft()

def recurse(c, m, i):
    values = []
    if c == 0:
        value = sum([i.popleft() for _ in range(m)])
        return (i, value)
    for j in range(c):
        new_c = i.popleft()
        new_m = i.popleft()
        i, value = recurse(new_c, new_m, i)
        values.append(value)
    
    value = 0
    for j in range(m):
        ref_node = i.popleft()
        value += values[ref_node - 1] if ref_node > 0 and ref_node <= len(values) else 0
    return (i, value)

_, val = recurse(children, metadata, inp_p2)
val