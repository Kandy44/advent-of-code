import sys
from itertools import combinations


def are_collinear(p1, p2, p3):
    return (p3[1] - p2[1]) * (p2[0] - p1[0]) == (p2[1] - p1[1]) * (p3[0] - p2[0])


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def antinode_idxs(p1, p2, r, c, check_dist, part_2):
    valid_idxs = set()
    for i in range(r):
        for j in range(c):
            p3 = (i, j)
            d1 = dist(p1, p3)
            d2 = dist(p2, p3)
            collinear = are_collinear(p1, p2, p3)
            if part_2:
                if collinear:
                    valid_idxs.add(p3)
            elif collinear and ((d2 == check_dist * d1) or (d1 == check_dist * d2)):
                valid_idxs.add(p3)
    return valid_idxs


def get_unique_antinodes(grid, start_multiple, end_multiple, part_2):
    r, c = len(grid), len(grid[0])
    freq_idxs = {}
    for i in range(len(grid)):
        for j, ch in enumerate(grid[i]):
            if ch.isalpha() or ch.isdigit():
                freq_idxs[ch] = freq_idxs.get(ch, []) + [(i, j)]

    freq_count = {}
    for idxs in freq_idxs.values():
        for multiple in range(start_multiple, end_multiple + 1):
            for p1, p2 in combinations(idxs, r=2):
                cur_antinodes = antinode_idxs(p1, p2, r, c, multiple, part_2)
                for p in cur_antinodes:
                    freq_count[p] = freq_count.get(p, 0) + 1
    return len(freq_count)


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = []
        for line in fp.readlines():
            lines.append(line.strip("\n"))
        return lines


def main():
    filename = sys.argv[1]
    grid = read_data(filename)
    part_1_ans = get_unique_antinodes(grid, 2, 2, False)
    part_2_ans = get_unique_antinodes(grid, 0, len(grid), True)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
