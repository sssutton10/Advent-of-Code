with open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day01.txt', 'r') as f:
    nums = f.readlines()

l1 = [None] * len(nums)
l2 = [None] * len(nums)

for i, n in enumerate(nums):
    n1, n2 = n.split('   ')
    l1[i] = int(n1)
    l2[i] = int(n2)
    
l1 = sorted(l1)
l2 = sorted(l2)

print(sum([abs(x - y) for x, y in zip(l1, l2)]))

p2 = 0
for x in l1:
    p2 += x * l2.count(x)
print(p2)