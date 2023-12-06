# Part-1: 840336
# Part-2: 41382569

import sys
import re
import math


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        times, distances = [list(map(int, re.findall(r"\d+", fp.readline()))) for _ in range(2)]
    return [times, distances]


def count_possibilities(times, distances):
    return math.prod([cur_count for cur_time, cur_dist in zip(times, distances) if(cur_count := sum((cur_time - i) * i > cur_dist for i in range(1, cur_time)))> 0])


def day_6(data):
    times, distances = data
    part_1 = count_possibilities(times, distances)
    new_times = [int("".join(map(str, times)))]
    new_distances = [int("".join(map(str, distances)))]
    part_2 = count_possibilities(new_times, new_distances)
    return (part_1, part_2)


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    part_1_ans, part_2_ans = day_6(data)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
