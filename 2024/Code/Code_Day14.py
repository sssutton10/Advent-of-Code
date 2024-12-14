import re

class Robot:
    x_max = 101
    y_max = 103
    def __init__(self, nums):
        self.x = nums[0]
        self.y = nums[1]
        self.dx = nums[2]
        self.dy = nums[3]
        
    def move_robot(self, n):
        self.x = (self.x + self.dx * n) % self.x_max
        self.y = (self.y + self.dy * n) % self.y_max

q1, q2, q3, q4 = 0, 0, 0, 0
quad_width = 101 // 2
quad_height = 103 // 2
 
robots = [x.strip() for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day14.txt', 'r')]
bots_p2 = []
for r in robots:
    nums = [int(x) for x in re.findall('-?\d+', r)]
    r = Robot(nums)
    bots_p2.append(Robot(nums))
    r.move_robot(100)
    q1 += 1 if r.x < quad_width and r.y < quad_height else 0
    q2 += 1 if r.x > (quad_width) and r.y < quad_height else 0
    q3 += 1 if r.x < quad_width and r.y > (quad_height) else 0
    q4 += 1 if r.x > (quad_width) and r.y > (quad_height) else 0

print(q1 * q2 * q3 * q4)

# Part 2
def move_robots(blist, f):
    spots = set()
    for bot in blist:
        bot.move_robot(1)
        spots.add((bot.x, bot.y))
    for i in range(103):
        s = ''
        for j in range(101):
            if (j, i) in spots:
                s += '#'
            else:
                s += '.'
        f.write(s + '\n')
    return blist

f = open('C:/Users/sssut/Documents/robots.txt', 'a')
for _ in range(10000):
    f.write(str(_) + '\n')
    bots_p2 = move_robots(bots_p2, f)
f.close()