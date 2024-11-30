from collections import defaultdict

with open('Input/2023/Day_15.txt') as f:
    inp = f.read().split(',')

def run_hash(x):
    val = 0
    for c in x:
        val = (val + ord(c)) * 17
        val = val % 256
    return val

p1 = 0
for hs in inp:
    p1 += run_hash(hs)
print(p1)

boxes = defaultdict(list)
for hs in inp:
    if '=' in hs:
        lab, lens = hs.split('=')
        box_num = run_hash(lab)
        if lab not in [ll[0] for ll in boxes[box_num]]:
            boxes[box_num].append((lab, int(lens)))
        else:
            ind = sum([i for i in range(len(boxes[box_num])) if boxes[box_num][i][0] == lab])
            boxes[box_num][ind] = (lab, int(lens))
    if '-' in hs:
        lab, lens = hs.split('-')
        box_num = run_hash(lab)
        if lab in [ll[0] for ll in boxes[box_num]]:
            boxes[box_num] = [x for x in boxes[box_num] if x[0] != lab]
           
p2 = 0
for box, lenses in boxes.items():
    for lab, lens in lenses:
        p2 += (1 + box) * (lenses.index((lab, lens)) + 1) * lens
print(p2)