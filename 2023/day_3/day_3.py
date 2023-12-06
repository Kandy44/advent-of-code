# Part-1 : 539637
# Part-2 : 82818007
import math
import sys


def read_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            data.append(list(line.strip("\n")))
    return data


def check_idx(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def part_number(data, num_idxs, n, m):
    row_num, i, j = num_idxs
    for x in range(row_num - 1, row_num + 2):
        for y in range(i - 1, j + 2):
            if check_idx(x, y, n, m):
                if data[x][y] != "." and not data[x][y].isdigit():
                    return [data[x][y], x, y]
    return []


def day_3(data):
    gears_dict = {}
    part_1_ans = 0
    part_2_ans = 0

    n, m = len(data), len(data[0])
    for row_num, row in enumerate(data):
        num = ""
        i = -1
        for idx, ch in enumerate(row):
            if ch.isdigit():
                if i == -1:
                    i = idx
                num = num + ch
            else:
                if num != "":
                    symbol_found = part_number(data, [row_num, i, idx - 1], n, m)
                    if symbol_found:
                        part_1_ans += int(num)
                    if symbol_found and symbol_found[0] == "*":
                        idx_pair = (symbol_found[1], symbol_found[2])
                        gears_dict[idx_pair] = gears_dict.get(idx_pair, []) + [int(num)]
                    num = ""
                    i = -1
        if num != "":
            symbol_found = part_number(data, [row_num, i, m - 1], n, m)
            if symbol_found:
                part_1_ans += int(num)
            if symbol_found and symbol_found[0] == "*":
                idx_pair = (symbol_found[1], symbol_found[2])
                gears_dict[idx_pair] = gears_dict.get(idx_pair, []) + [int(num)]
            num = ""

    for v in gears_dict.values():
        if len(v) == 2:
            part_2_ans += math.prod(v)
    return [part_1_ans, part_2_ans]


def main():
    filename = sys.argv[1]
    data = read_data(filename)

    part_1_ans, part_2_ans = day_3(data)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


main()
