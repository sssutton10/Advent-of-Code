forklift_inp = [y.strip() for y in open('Day_4.txt', 'r').readlines()]

forklift_map = {}
paper_spots = set()
for i, line in enumerate(forklift_inp):
    for j, x in enumerate(line):
        forklift_map[complex(j, i)] = x
        if x == '@':
            paper_spots.add(complex(j, i))

# Part 1
removable_papers = set()
adj_deltas = [-1, 1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]

for pos in paper_spots:
    if forklift_map[pos] == '@' and sum([1 if forklift_map.get(pos + delta, '.') == '@' else 0 for delta in adj_deltas]) < 4:
        removable_papers.add(pos)
print(len(removable_papers))

# Part 2
total_removed = len(removable_papers)

while len(removable_papers) > 0:
    paper_spots = paper_spots - removable_papers
    for pos in removable_papers:
        forklift_map[pos] = '.'
    removable_papers = set()
    for pos in paper_spots:
        if forklift_map[pos] == '@' and sum([1 if forklift_map.get(pos + delta, '.') == '@' else 0 for delta in adj_deltas]) < 4:
            removable_papers.add(pos)
    total_removed += len(removable_papers)
print(total_removed)