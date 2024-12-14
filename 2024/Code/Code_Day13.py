import re

bas, bbs, ps, ps_p2 = [], [], [], []
for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day13.txt', 'r').readlines():
    for num in re.findall(r'\d+', x):
        if 'Button A' in x:
            bas.append(int(num))
        elif 'Button B' in x:
            bbs.append(int(num))
        elif 'Prize' in x:
            ps.append(int(num))
            ps_p2.append(int(num) + 10000000000000)

p1 = 0
for i in range(0, len(bas), 2):
    s1 = bas[i] / bas[i+1] * ps[i+1]
    s2 = bbs[i] - bbs[i+1] * bas[i] / bas[i+1]

    b_press = round((s1 - ps[i]) / (s2 * -1))
    if b_press > 100 or b_press < 0:
        continue

    a_press = (ps[i] - b_press * bbs[i]) / bas[i]
    if a_press > 100 or a_press < 0:
        continue

    if a_press * bas[i] + b_press * bbs[i] == ps[i] and a_press * bas[i+1] + b_press * bbs[i+1] == ps[i+1]:
        p1 += 3*round(a_press) + round(b_press)
print(p1)


p2 = 0

for i in range(0, len(bas), 2):
    s1 = bas[i] / bas[i+1] * ps_p2[i+1]
    s2 = bbs[i] - bbs[i+1] * bas[i] / bas[i+1]

    b_press = round((s1 - ps_p2[i]) / (s2 * -1))
    if b_press < 0:
        continue
    
    a_press = (ps_p2[i] - b_press * bbs[i]) / bas[i]
    if a_press < 0:
        continue

    if a_press * bas[i] + b_press * bbs[i] == ps_p2[i] and a_press * bas[i+1] + b_press * bbs[i+1] == ps_p2[i+1]:
        p2 += 3*round(a_press) + round(b_press)
print(p2)