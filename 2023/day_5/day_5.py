import sys
import re


def read_data(filename):
    lines = ""
    with open(filename, "r", encoding="utf-8") as fp:
        lines = "".join(fp.readlines())
    # data = lines.split("\n\n")
    data = []
    idx = 0
    for line in lines.split("\n\n"):
        cur_row = []
        for cur_line in line.split("\n"):
            # print(cur_line)
            nums_found = re.findall(r"\d+", cur_line)
            if nums_found:
                nums_found = list(map(int, nums_found))
                if idx == 0:
                    cur_row.append(nums_found)
                else:
                    # first_range = [nums_found[0], nums_found[0] + nums_found[2]]
                    # second_range = [nums_found[1], nums_found[1] + nums_found[2]]
                    second_range = [nums_found[0], nums_found[0] + nums_found[2]]
                    first_range = [nums_found[1], nums_found[1] + nums_found[2]]
                    cur_row.append(first_range + second_range)
        idx += 1
        data.append(cur_row)
    # print(data)
    return data


def find_location(seed, data):
    check_value = seed
    for part in data:
        for x1, y1, x2, _ in part:
            if x1 <= check_value <= y1:
                res = x2 + abs(x1 - check_value)
                check_value = res
                break
    return check_value


def part_1(data):
    seeds = data[0][0]
    min_location = sys.maxsize

    t = data[1:]
    for seed in seeds:
        min_location = min(min_location, find_location(seed, t))
    return min_location


def part_2(data):
    seeds = data[0][0]
    min_location = sys.maxsize
    t = data[1:]
    for i in range(0, len(seeds), 2):
        x, y = seeds[i], seeds[i] + seeds[i + 1]
        while x < y:
            min_location = min(min_location, find_location(x, t))
            x += 1

    return min_location


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    # print(data)
    # print(data[0])
    # print(data[1])

    # print(data[1])
    print(part_1(data))
    print(part_2(data))

    # for x1, y1, x2, y2 in data[1]:
    #     print(x1, y1, x2, y2)

    # part_1_ans, part_2_ans = day_5(data)
    # print(f"Part-1: {part_1_ans}")
    # print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
