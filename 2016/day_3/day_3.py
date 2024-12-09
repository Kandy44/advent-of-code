import sys
import re


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return [
            list(map(int, re.sub(r"\s+", " ", line.strip("\n")).split()))
            for line in fp.readlines()
        ]


def is_triangle(sides):
    tmp = sorted(sides)
    n = len(sides)
    return all(tmp[i] + tmp[(i + 1) % n] > tmp[(i + 2) % n] for i in range(n))


def part_1(spec):
    return sum(is_triangle(cur_sides) for cur_sides in spec)


def part_2(spec):
    transpose = zip(*spec)

    count = 0
    for row in list(transpose):
        for i in range(0, len(row), 3):
            sides = list(row[i : i + 3])
            if is_triangle(sides):
                count += 1
    return count


def main():
    filename = sys.argv[1]
    spec = read_data(filename)

    part_1_ans = part_1(spec)
    part_2_ans = part_2(spec)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
