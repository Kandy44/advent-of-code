# Part-1: 54634
# Part-2: 53855
import sys


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return [line.strip("\n") for line in fp.readlines()]


def day_1(data, convert=False):
    res = 0
    for line in data:
        digits = []
        for idx, ch in enumerate(line):
            if ch.isdigit():
                digits.append(ch)
            if convert:
                for num, val in enumerate(
                    "one, two, three, four, five, six, seven, eight, nine".split(", ")
                ):
                    if line[idx:].startswith(val):
                        digits.append(str(num + 1))
        res += int(digits[0] + digits[-1])
    return res


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    part_1_ans = day_1(data, convert=False)
    part_2_ans = day_1(data, convert=True)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


main()
