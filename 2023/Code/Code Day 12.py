import re
from functools import cache

with open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2023/Input Day 12.txt') as f:
    spring_list = f.readlines()

@cache
def spring_comb(s, n, k):
    if s.count('#') > sum(n):
        return 0
    if n == () and k == 0:
        return 1
    elif n == () and k != 0:
        return 0
    
    answer = 0
    blah = [x for x in re.finditer(re.compile(f'(?<!#)(?=([#?]{{{n[0]}}}[?\.]))'), s)]
    
    for mat in blah:
        start, end = mat.span(1)
        answer += spring_comb(s[end:], n[1:], k - mat.group(1).count('#'))   
        
    return answer

part1 = 0
part2 = 0

for i, row in enumerate(spring_list):
    springs, nums_txt = row.split()
    springs_long = '?'.join([springs] * 5) + '.'
    nums = eval(nums_txt)
    
    part1 += spring_comb(springs, nums, springs.count('#')) 
    part2 += spring_comb(springs_long, nums * 5, springs_long.count('#'))
    
print(part1)
print(part2)