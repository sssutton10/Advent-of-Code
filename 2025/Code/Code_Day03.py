banks = [[int(x) for x in list(y.strip())] for y in open('./Day_3.txt', 'r').readlines()]

# Part 1
joltage = 0
for bank in banks:
    index1 = bank.index(max(bank[:-1]))
    index2 = bank.index(max(bank[(index1 + 1):]))
    joltage += int(str(bank[index1]) + str(bank[index2]))
print(joltage)

# Part 2
joltage = 0
for bank in banks:
    final_num = ''
    while len(final_num) < 12:
        thresh = len(bank) - 11 + len(final_num)
        ind = bank.index(max(bank[:thresh]))
        final_num += str(bank[ind])
        bank = bank[ind + 1:]
    joltage += int(final_num)
print(joltage)