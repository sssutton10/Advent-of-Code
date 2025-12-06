import re

coords = [[int(x) for x in re.findall(r'-?[\d]+', y)] for y in open('Day_10.txt', 'r').readlines()]
vels = {}
positions = {}
for i, coord in enumerate(coords):
    positions[i] = complex(coord[0], coord[1])
    vels[i] = complex(coord[2], coord[3])

# Part 1 and 2
time = 1
while True:
    for k in positions:
        positions[k] += vels[k]
    min_x = min(v.real for v in positions.values())
    max_x = max(v.real for v in positions.values())
    min_y = min(v.imag for v in positions.values())
    max_y = max(v.imag for v in positions.values())
   
    if (max_y - min_y) < 15:
        print(time)
        break
    time += 1

for y in range(int(min_y)-3, int(max_y) + 4):
    str = ''
    for x in range(int(min_x)-3, int(max_x) + 4):
        if complex(x, y) in positions.values():
            str += '#'
        else:
            str += '.'
    print(str)