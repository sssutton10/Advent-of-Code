reports = [[int(y) for y in x.split()] for x in open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day02.txt', 'r').readlines()]

p1 = 0
p2 = 0

def check_report(report, inc):
    if inc == 1:
        return [1 if 3 >= report[i+1]-report[i] >= 1 else 0 for i in range(len(report) - 1)]
    else:
        return [1 if (-3 <= (report[i+1]-report[i]) <= -1) else 0 for i in range(len(report) - 1)]

# Part 1
for x in reports:
    incr = 1 if x[1] > x[0] else -1
    p1 += 1 if sum(check_report(x, incr)) == (len(x) - 1) else 0    

print(p1)

# Part 2 - not efficient based on part 1
for x in reports:
    diffs = [x[i + 1] - x[i] for i in range(len(x) - 1)]
    incs = [1 if y > 0 else -1 if y < 0 else 0 for y in diffs]
    inc = 1 if sum(incs) > 0 else -1

    if sum(check_report(x, inc)) == (len(x) - 1):
        p2 += 1
    else:
        for j in range(len(x)):
            if sum(check_report(x[:j] + x[j+1:], inc)) == (len(x) - 2):
                p2 += 1
                break
print(p2)