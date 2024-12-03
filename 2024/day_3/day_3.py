import re
import sys

mul_regex = r"mul\(\d+, ?\d+\)"
sub_regex = r"mul\((\d+), ?(\d+)\)"
all_instructions_regex = r"mul\(\d+, ?\d+\)|(don\'t\(\))|(do\(\))"


def multiply_matches(matches):
    sub_matches = "+".join(
        [re.sub(sub_regex, r"(\1 * \2)", match, 0) for match in matches]
    )
    return eval(sub_matches)


def part_1(data):
    matches = re.findall(mul_regex, data)
    return multiply_matches(matches)


def part_2(data):
    matches = re.finditer(all_instructions_regex, data)
    is_enabled = True
    filtered_matches = []
    for match in matches:
        if match.group() == "don't()":
            is_enabled = False
            continue
        if match.group() == "do()":
            is_enabled = True
            continue
        if is_enabled:
            filtered_matches.append(match.group())

    return multiply_matches(filtered_matches)


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return "".join([row.strip("\n") for row in fp.readlines()])


def main():
    filename = sys.argv[1]
    rows = read_data(filename)
    part_1_ans, part_2_ans = part_1(rows), part_2(rows)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
