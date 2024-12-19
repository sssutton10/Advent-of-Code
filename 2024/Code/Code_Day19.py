from functools import cache

towels, designs = open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day19.txt').read().split('\n\n')
towels = towels.split(', ')
designs = designs.split('\n')

@cache
def recurse(design):
    if design == '':
        return 1
    ret = 0
    for towel in towels:
        if design.startswith(towel):
            ret += recurse(design[len(towel):])
    return ret

totals = []
for design in designs:
    totals.append(recurse(design))
    
sum(min(x, 1) for x in totals)
sum(totals)