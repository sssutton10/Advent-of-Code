mirrors = list(map(str.split, open('C:/Users/sssut/Documents/Python Scripts/Advent of Code/2023/Inputs/Input Day 13.txt').read().split('\n\n')))
mirrors

p1 = 0
for val in mirrors:
    for i in range(len(val) - 1):
        rows_to_match = min(i + 1, len(val) - (i + 1))
        check = 0
        for j in range(rows_to_match):
            if val[i - j] == val [i + 1 + j]:
                check += 1
        if check == rows_to_match:
            p1 += (i + 1) * 100
            break
    
    refl = [[x[i] for x in val] for i in range(len(val[0]))]
    for i in range(len(refl) - 1):
        rows_to_match = min(i + 1, len(refl) - (i + 1))
        check = 0
        for j in range(rows_to_match):
            if refl[i - j] == refl [i + 1 + j]:
                check += 1
        if check == rows_to_match:
            p1 += (i + 1)
            break

print(p1)

def count_mismatches(a, b):
    return sum([a[i] != b[i] for i in range(len(a))])

p2 = 0
for val in mirrors:
    for i in range(len(val) - 1):
        rows_to_match = min(i + 1, len(val) - (i + 1))
        check = 0
        check1 = 0
        for j in range(rows_to_match):
            mismatches = count_mismatches(val[i - j], val [i + 1 + j])
            if mismatches == 0:
                check += 1
            if mismatches == 1:
                check1 += 1
        if (rows_to_match - check) == 1 and check1 == 1:
            p2 += (i + 1) * 100
            break
    
    refl = [[x[i] for x in val] for i in range(len(val[0]))]
    for i in range(len(refl) - 1):
        rows_to_match = min(i + 1, len(refl) - (i + 1))
        check = 0
        check1 = 0
        for j in range(rows_to_match):
            mismatches = count_mismatches(refl[i - j], refl [i + 1 + j])
            if mismatches == 0:
                check += 1
            if mismatches == 1:
                check1 += 1
        if (rows_to_match - check) == 1 and check1 == 1:
            p2 += (i + 1)
            break

print(p2)   