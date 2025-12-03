with open('./Day_5.txt', 'r') as f:
    polymer_raw = [*f.read().strip()]

# Part 1
polymer = polymer_raw

keep = []
for i in range(len(polymer)):
    if len(keep) == 0 or abs(ord(polymer[i]) - ord(keep[-1])) != 32:
        keep.append(polymer[i])
    elif abs(ord(polymer[i]) - ord(keep[-1])) == 32:
        bye_bye = keep.pop()
print(len(keep))
       
# Part 2
min_length = 999999999
for char_code in range(ord('a'), ord('z') + 1):
    polymer = [x for x in polymer_raw if ord(x) != char_code and ord(x) != char_code - 32]
   
    keep = []
    for i in range(len(polymer)):
        if len(keep) == 0 or abs(ord(polymer[i]) - ord(keep[-1])) != 32:
            keep.append(polymer[i])
        elif abs(ord(polymer[i]) - ord(keep[-1])) == 32:
            bye_bye = keep.pop()
    min_length = min(min_length, len(keep))
print(min_length)
