inp = {}
for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day07.txt', 'r').readlines():
    val, calibs = x.strip().split(':')
    inp[int(val.strip())] = [int(y) for y in calibs.strip().split(' ')]

def recurse(l, t, s):
    if s > t:
        return 0
    if len(l) == 0:
        return t if s == t else 0
    return max(recurse(l[1:], t, s*l[0]), recurse(l[1:], t, s+l[0]))

p1 = 0
for k in inp:
    p1 += recurse(inp[k][1:], k, inp[k][0])

print(p1)

# Part 2
def recurse(l, t, s):
    if s > t:
        return 0
    if len(l) == 0:
        return t if s == t else 0
    return max(recurse(l[1:], t, s*l[0]), recurse(l[1:], t, s+l[0]), recurse(l[1:], t, int(str(s) + str(l[0]))))

p2 = 0
for k in inp:
    p2 += recurse(inp[k][1:], k, inp[k][0])

print(p2)