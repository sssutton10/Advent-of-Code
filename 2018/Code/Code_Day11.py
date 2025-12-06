serial_number = 1

coords = {}
for x in range(1, 301):
    for y in range(1, 301):
        rack_id = x + 10
        power_level = ((rack_id * y) + serial_number) * rack_id
        power_level = (power_level // 100) % 10 - 5
        coords[complex(x, y)] = power_level

# Part 1

max_power = -999
best_coord = None
adj_deltas = [-1, 1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
for coord in coords:
    if coord.real == 300 or coord.real == 1 or coord.imag == 300 or coord.imag == 1:
        continue
    total_power = coords[coord] + sum([coords[coord + delta] for delta in adj_deltas])
    if total_power > max_power:
        max_power = total_power
        best_coord = coord + (-1 - 1j)
print(best_coord)

# Part 2
# Let's assume we only need to check up through 75
max_power_p2 = -999
ans_p2 = None

for coord in coords:
    for i in range(3, 76):
        if coord.real + i > 300 or coord.imag + i > 300:
            break
        if i == 3:
            curr_power = sum([coords[coord + complex(x, y)] for x in range(3) for y in range(3)])
        else:
            curr_power += sum([coords[coord + complex(i-1, y)] for y in range(i)]) + sum([coords[coord + complex(y, i-1)] for y in range(i-1)])
        if curr_power > max_power_p2:
            max_power_p2 = curr_power
            ans_p2 = [coord, i]
print(ans_p2)

# LOL this is so bad