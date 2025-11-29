from collections import defaultdict

steps = [(x[5], x[36]) for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2018/Inputs/Input_Day07.txt', 'r').readlines()]

# Part 1
orders = defaultdict(set)
unique_steps = set()

for step in steps:
    orders[step[1]].add(step[0])
    unique_steps.add(step[0])
    unique_steps.add(step[1])

queue = sorted([x for x in unique_steps if x not in orders])
final_order = ''
while len(queue) > 0:
    next_order = queue[0]
    final_order += next_order
    
    add_to_queue = []
    for k, v in orders.items():
        v.discard(next_order)
        if len(v) == 0:
            add_to_queue.append(k)
    for order in add_to_queue:
        del orders[order]
    
    queue = sorted(queue[1:] + add_to_queue)
print(final_order)

# Part 2
orders = defaultdict(set)
unique_steps = set()

for step in steps:
    orders[step[1]].add(step[0])
    unique_steps.add(step[0])
    unique_steps.add(step[1])

queue = sorted([x for x in unique_steps if x not in orders], reverse = True)
final_order_p2 = ''
workers = {k: (None, 0) for k in range(1, 6)}
time = -1

while len(final_order) > len(final_order_p2):
    finished = []
    for k, v in workers.items():
        if v[0] and v[1] == 1:
            final_order_p2 += v[0]
            finished.append(v[0])
            workers[k] = (None, 0)
    
    add_to_queue = []
    for k, v in orders.items():
        for f in finished:
            v.discard(f)
            if len(v) == 0:
                add_to_queue.append(k)
    for order in add_to_queue:
        del orders[order]
    
    queue = sorted(queue + add_to_queue, reverse = True)
    
    for k, v in workers.items():
        if not v[0] and len(queue) > 0:
            next_order = queue.pop()
            workers[k] = (next_order, ord(next_order) - 4)
        else:
            workers[k] = (v[0], max(v[1] - 1, 0))
    
    time += 1
print(time)
    