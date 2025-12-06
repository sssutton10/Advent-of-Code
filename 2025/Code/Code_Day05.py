inp = open('Day_5.txt', 'r').read().split('\n\n')
ranges = [[int(x) for x in r.split('-')] for r in inp[0].split('\n')]
vals = [int(x) for x in inp[1].split('\n')]

# Part 1
fresh = 0
for val in vals:
    for r in ranges:
        if r[0] <= val <= r[1]:
            fresh += 1
            break
print(fresh)
   
# Part 2
ranges_sorted = sorted(ranges, key=lambda x: x[0])
final_ranges = [ranges_sorted[0]]
for r in ranges_sorted[1:]:
    added = False
    for f in final_ranges:
        if r[0] > f[1] or r[1] < f[0]:
            continue
        if r[0] >= f[0] and r[1] <= f[1]:
            added = True
            break
        elif r[0] < f[0] and r[1] >= f[0]:
            added = True
            f[0] = r[0]
        elif r[1] > f[1] and r[0] <= f[1]:
            added = True
            f[1] = r[1]
    if not added:
        final_ranges.append(r)
print(sum([r[1] - r[0] + 1 for r in final_ranges]))