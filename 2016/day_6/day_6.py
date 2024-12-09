import sys
from collections import Counter


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return [list(line.strip("\n")) for line in fp.readlines()]


def day_6(data, is_part_2):
    transpose = list(zip(*data))
    idx = -1 if is_part_2 else 0
    return "".join(Counter(row).most_common()[idx][0] for row in transpose)


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    part_1_ans = day_6(data, False)
    part_2_ans = day_6(data, True)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
