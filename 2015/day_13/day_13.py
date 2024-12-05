import sys
import re
from itertools import permutations

NAMES_REG = r"(.+) would .+ (\d+) .+ (.+)\."
NAME_REG = r"(.+) would"


def part_1(data):
    pair_dict = {}
    names = set()
    for row in data:
        name1, val, name2 = re.findall(NAMES_REG, row)[0]
        val = int(val)
        if "lose" in row:
            val = -val
        names.add(name1)
        pair_dict[(name1, name2)] = val

    max_happiness = 0
    for perm in permutations(names):
        cur_perm_names = perm

        cur_perm_happiness = sum(
            pair_dict[(cur_perm_names[i], cur_perm_names[i + 1])]
            for i in range(0, len(perm) - 1)
        )

        cur_perm_happiness += sum(
            pair_dict[(cur_perm_names[i + 1], cur_perm_names[i])]
            for i in range(0, len(perm) - 1)
        )

        cur_perm_happiness += pair_dict[(cur_perm_names[0], cur_perm_names[-1])]
        cur_perm_happiness += pair_dict[(cur_perm_names[-1], cur_perm_names[0])]
        max_happiness = max(max_happiness, cur_perm_happiness)

    return max_happiness


def part_2(data):
    names = set()
    for row in data:
        name1 = re.findall(NAME_REG, row)[0]
        names.add(name1)

    new_name_data = [
        f"{name} would gain 0 happiness units by sitting next to Kandy."
        for name in names
    ] + [
        f"Kandy would lose 0 happiness units by sitting next to {name}."
        for name in names
    ]

    new_data = data + new_name_data

    return part_1(new_data)


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = [line.strip("\n") for line in fp.readlines()]
        return lines


def main():
    filename = sys.argv[1]
    data = read_data(filename)

    part_1_ans, part_2_ans = part_1(data), part_2(data)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
