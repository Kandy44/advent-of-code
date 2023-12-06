# Part-1: 23235
# Part-2: 5920640

from collections import defaultdict
import sys
import re


def read_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            part_1, part_2 = line.strip("\n").split(": ")[1].split(" | ")
            winning_numbers = re.findall(r"\d+", part_1)
            existing_numbers = re.findall(r"\d+", part_2)
            common_nums = len(set(winning_numbers) & set(existing_numbers))
            data.append(common_nums)
    return data


def day_4(data):
    part_1_ans = 0
    res_dict = defaultdict(int)

    for card_num, common_nums in enumerate(data):
        res_dict[card_num] += 1
        score = 2 ** (common_nums - 1) if common_nums > 0 else 0
        part_1_ans += score
        for j in range(common_nums):
            res_dict[card_num + j + 1] += res_dict[card_num]
    return (part_1_ans, sum(res_dict.values()))


def main():
    filename = sys.argv[1]
    data = read_data(filename)

    part_1_ans, part_2_ans = day_4(data)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


main()
