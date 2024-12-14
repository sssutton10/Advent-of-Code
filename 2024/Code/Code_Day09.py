disk = open("C:/Users/sssut/Documents/Python Scripts/Advent of Code/2024/Inputs/Input_Day09.txt", "r").read().strip()

def map_disk(disk):
    is_file = True
    id = 0
    ret_val = []
    for x in disk:
        for _ in range(int(x)):
            if is_file:
                ret_val.append(id)
            else:
                ret_val.append(".")
        if is_file:
            id += 1
        is_file = not is_file
    return list(ret_val)

def compress(map_disk):
    map_copy = []
    for x in map_disk:
        if x != ".":
            map_copy.append(x)
        else:
            while True:
                block = map_disk.pop()
                if block != ".":
                    break
            map_copy.append(block)
    return map_copy

def get_free_spaces(disk):
    free_space = {}
    ind = 0
    is_space = False
    for x in disk:
        if is_space:
            free_space[ind] = int(x)
        is_space = not is_space
        ind += int(x)
    return free_space

# This is so bad and really needs to be better
def compress_p2(disk, md):
    md = map_disk(disk)
    map_copy = md.copy()
    fs = get_free_spaces(disk)

    check_vals = sorted(set([x for x in md if x != "."]), reverse=True)
    first_incs = [md.index(x) for x in check_vals]

    for s, x in enumerate(check_vals):
        file_size = md.count(x)
        moved = False
        for y in sorted(fs):
            if y > first_incs[s]:
                break

            if y < first_incs[s] and fs[y] >= file_size:
                moved = True
                for i in range(y, y + file_size):
                    map_copy[i] = x
                for i in range(first_incs[s], first_incs[s] + file_size):
                    map_copy[i] = "."
                break

        if moved:
            fs[y + file_size] = fs[y] - file_size
            del fs[y]
        moved = False

    return map_copy

sum([i * int(x) for i, x in enumerate(compress(map_disk(disk)))])
sum([i * int(x) for i, x in enumerate(compress_p2(disk, map_disk(disk))) if x != "."])
