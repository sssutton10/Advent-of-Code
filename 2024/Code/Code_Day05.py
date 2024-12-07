from collections import defaultdict

# Parts 1 and 2
reqs = defaultdict(list)
manuals = []
for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day05.txt', 'r').readlines():
    if x.strip() == '':
        continue
    if '|' in x:
        before, after = x.strip().split('|')
        reqs[int(before)].append(int(after))
    else:
         manuals.append([int(y) for y in x.strip().split(',')])

def check_pages(curr_page, pages, reqs):
    for page in pages:
        if curr_page in reqs[page]:
            return False
    return True

def reorder(pages, reqs):
    new_l = []
    while len(pages) > 0:
        for i, x in enumerate(pages):
            if any(x in reqs[y] for y in pages[(i+1):]):
                continue
            else:
                pages.remove(x)
                new_l.append(x)
                break
    return new_l
p1 = 0
p2 = 0

for m in manuals:
    valid = True
    for i in range(len(m) - 1):
        if not check_pages(m[i], m[(i+1):], reqs):
            valid = False
            break
    if valid:
        p1 += m[int((len(m) - 1) / 2)]
    else:
        new_order = reorder(m, reqs)
        p2 += new_order[int((len(new_order) - 1) / 2)]

print(p1)
print(p2)