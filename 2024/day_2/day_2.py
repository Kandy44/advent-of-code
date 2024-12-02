import sys


def is_inc(lst):
    return all(lst[i] < lst[i + 1] for i in range(0, len(lst) - 1))


def is_dec(lst):
    return all(lst[i] > lst[i + 1] for i in range(0, len(lst) - 1))


def is_safe(lst):
    if not (is_inc(lst) or is_dec(lst)):
        return False
    return all(1 <= abs(lst[j] - lst[j + 1]) <= 3 for j in range(0, len(lst) - 1))


def part_1(data):
    return sum(is_safe(row) for row in data)


def part_2(data):
    count = 0
    for row in data:
        if any(is_safe(row[:j] + row[j + 1 :]) for j in range(len(row))):
            count += 1
    return count


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        rows = [list(map(int, row.split(" "))) for row in fp.readlines()]
    return rows


def main():
    filename = sys.argv[1]
    rows = read_data(filename)
    part_1_ans, part_2_ans = part_1(rows), part_2(rows)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
