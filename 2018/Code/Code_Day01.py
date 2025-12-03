freqs = [int(y.replace('+', '')) for y in open('./Day_1.txt', 'r').readlines()]

# Part 1
print(sum(freqs))

# Part 2
def find_first_repeated_frequency(freqs):
    seen = set()
    current = 0
    while True:
        for f in freqs:
            current += f
            if current in seen:
                return current
            seen.add(current)

print(find_first_repeated_frequency(freqs))