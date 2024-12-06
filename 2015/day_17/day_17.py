from itertools import combinations
import sys


def part_1(containers, req_liters):
    count = 0
    for i in range(1, len(containers)):
        for comb in combinations(containers, r=i):
            if sum(comb) == req_liters:
                count += 1
    return count


def part_2(containers, req_liters):
    comb_length_counts = {}
    for i in range(1, len(containers)):
        comb_length_counts[i] = 0
        for comb in combinations(containers, r=i):
            if sum(comb) == req_liters:
                comb_length_counts[i] += 1

    min_length_container_combinations = next(
        (
            comb_length_counts[i]
            for i in sorted(comb_length_counts)
            if comb_length_counts[i] > 0
        ),
        0,
    )
    return min_length_container_combinations


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = [int(line.strip("\n")) for line in fp.readlines()]
        return lines


def main():
    filename = sys.argv[1]
    containers = read_data(filename)
    req_liters = 150

    part_1_ans, part_2_ans = (
        part_1(containers, req_liters),
        part_2(containers, req_liters),
    )
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
