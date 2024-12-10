import sys
import numpy as np


def part_1(total_houses):
    houses = np.array([10 for _ in range(total_houses)])
    for i in range(2, (total_houses // 10)):
        # Update all multiples
        houses[i::i] += 10 * i
    return (houses > total_houses).argmax()


def part_2(total_houses):
    houses = np.array([10 for _ in range(total_houses)])
    for i in range(2, (total_houses // 10)):
        # Update only first 50 multiples
        houses[i : (50 * i) + 1 : i] += 11 * i
    return (houses > total_houses).argmax()


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return int("".join([line.strip("\n") for line in fp.readlines()]))


def main():
    filename = sys.argv[1]
    total_houses = read_data(filename)
    part_1_ans = part_1(total_houses)
    part_2_ans = part_2(total_houses)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
