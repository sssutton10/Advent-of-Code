import re

# Part 1
prog = ''.join(open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day03.txt', 'r').readlines())
muls = re.findall(re.compile('mul\\([0-9]{1,3},[0-9]{1,3}\\)'), prog)
p1 = 0
for mul in muls:
    y = re.findall(re.compile('\d+'), mul)
    p1 += int(y[0]) * int(y[1])
print(p1)

# Part 2
p2 = 0

dos = [0] + [int(x.end()) for x in re.finditer(re.compile("do\(\)"), prog)]
donts = [int(x.end()) for x in re.finditer(re.compile("don't\(\)"), prog)] + [len(prog)]

spans = []
while len(dos) > 0:
    span_start = dos.pop(0)
    while True:
        span_end = donts.pop(0)
        if span_end > span_start:
            break
   
    if len(dos) > 0:
        while True:
            if dos[0] > span_end:
                break
            dos.pop(0)
   
    spans.append((span_start, span_end))

for span in spans:
    muls = re.findall(re.compile('mul\\([0-9]{1,3},[0-9]{1,3}\\)'), prog[span[0]:(span[1])])
    for mul in muls:
        y = re.findall(re.compile('\d+'), mul)
        p2 += int(y[0]) * int(y[1])
print(p2)