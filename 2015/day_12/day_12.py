import sys
import json
import re

NUMS_REGEX = r"-?\d+"


def part_1(data):
    return sum(map(int, re.findall(NUMS_REGEX, data)))


def hook_fn(d):
    # If red is found in any of the value, return empty dict
    # Else, return the original dict
    return {} if "red" in d.values() else d


def part_2(data):
    filtered_json_data = str(json.loads(data, object_hook=hook_fn))
    return part_1(filtered_json_data)


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = [line.strip("\n") for line in fp.readlines()]
        return "".join(lines)


def main():
    filename = sys.argv[1]
    data = read_data(filename)

    part_1_ans, part_2_ans = part_1(data), part_2(data)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
