import sys


def part_1(row1, row2):
    return sum(abs(num1 - num2) for num1, num2 in zip(row1, row2))


def part_2(row1, row2):
    return sum(num1 * row2.count(num1) for num1 in row1)


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        rows = [list(map(int, row.split("   "))) for row in fp.readlines()]
        nested_lists = [sorted(row) for row in zip(*rows)]
    return nested_lists


def main():
    filename = sys.argv[1]
    rows = read_data(filename)
    part_1_ans, part_2_ans = part_1(*rows), part_2(*rows)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
