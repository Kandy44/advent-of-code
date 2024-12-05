import sys
from itertools import combinations
from functools import cmp_to_key


def all_comb_res(rules, update):
    parts = update.split(",")
    for c in combinations(parts, 2):
        if "|".join(c) not in rules:
            return 0
    return int(parts[len(parts) // 2])


def sort_update_res(update, key):
    parts = list(map(int, update.split(",")))
    parts.sort(key=key)
    return int(parts[len(parts) // 2])


def part_1(rules, updates):
    count = 0
    for update in updates:
        count += all_comb_res(rules, update)
    return count


def part_2(rules, updates):
    count = 0
    rules_set = set([tuple(map(int, rule.split("|"))) for rule in rules])

    def cmp_fun(a, b):
        if (a, b) in rules_set:
            return 1
        elif (b, a) in rules_set:
            return -1
        return 0

    key = cmp_to_key(cmp_fun)

    for update in updates:
        if all_comb_res(rules, update) == 0:
            count += sort_update_res(update, key)

    return count


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = [line.strip("\n") for line in fp.readlines()]
        idx = next(i for i in range(len(lines)) if lines[i] == "")
        rules, updates = lines[:idx], lines[idx + 1 :]
        return [rules, updates]


def main():
    filename = sys.argv[1]
    rules, updates = read_data(filename)
    part_1_ans, part_2_ans = part_1(rules, updates), part_2(rules, updates)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
