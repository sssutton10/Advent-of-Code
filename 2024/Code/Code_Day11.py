
from collections import defaultdict

stones = defaultdict(int, {int(x.strip()):1 for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day11.txt', 'r').read().split()})

def blink(stones):
    new_stones = defaultdict(int)
    for s in stones:
        if s == 0:
            new_stones[1] += stones[s]
        elif len(str(s)) % 2 == 0:
            num_str = str(s)
            num1 = int(num_str[:(len(num_str) // 2)])
            num2 = int(num_str[(len(num_str) // 2):])
            
            new_stones[num1] += stones[s]
            new_stones[num2] += stones[s]
        else:
            new_stones[s * 2024] += stones[s]
    return new_stones

for _ in range(75):
    stones = blink(stones)
    
sum([x for x in stones.values()])