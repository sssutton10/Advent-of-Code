import re

inp = [[int(x) for x in y.split('-')] for y in open('./Input_Day02.txt', 'r').read().split(',')]

# Part 1 and 2
p1 = 0
p2 = 0
for x, y in inp:
    for val in range(x ,y + 1):
        if re.match(r'^(.+)\1$', str(val)):
            p1 += val
        if re.match(r'^(.+)\1+$', str(val)):
            p2 += val
print(p1)
print(p2)
        
        
                
