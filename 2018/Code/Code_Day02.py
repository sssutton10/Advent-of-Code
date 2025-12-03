from collections import Counter

boxes = [y.strip() for y in open('./Day_2.txt', 'r').readlines()]

# Part 1
twos = 0
threes = 0
for id in boxes:
    counts = Counter(id)
    twos += 1 if 2 in counts.values() else 0
    threes += 1 if 3 in counts.values() else 0
print(twos * threes)

# Part 2
def compare_boxes(box1, box2):
    return [i for i in range(len(box1)) if box1[i] != box2[i]]

def find_fabrics(box_list):
    for i in range(len(box_list)):
        for j in range(i + 1, len(box_list)):
            comp = compare_boxes(box_list[i], box_list[j])
            if len(comp) == 1:
                return ''.join(box_list[i][:comp[0]]) + ''.join(box_list[i][(comp[0]+1):])
print(find_fabrics(boxes))