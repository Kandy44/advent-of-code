# Part-1: 2239
# Part-2: 83435
from math import prod
import sys


def read_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            line = line.strip("\n")
            game_num, rem = line.split(": ")
            game_num = int(game_num.split(" ")[-1])
            data.append([game_num, [row.split(", ") for row in rem.split("; ")]])
    return data


def get_cube_count(row_data):
    cube_count = {}
    for cube in row_data:
        count, color = cube.split(" ")
        cube_count[color] = cube_count.get(color, 0) + int(count)
    return cube_count


def day_2(data, cubes_count, calculate_power=False):
    res = 0
    for game_num, game_data in data:
        check = True
        max_values = {color: 0 for color in cubes_count.keys()}
        for row in game_data:
            cube_count = get_cube_count(row)
            for color in max_values.keys():
                max_values[color] = max(cube_count.get(color, 0), max_values[color])
            if not all(
                cube_count.get(color, 0) <= cubes_count.get(color, 0)
                for color in cubes_count.keys()
            ):
                check = False
        if calculate_power:
            res += prod(max_values.values())
        else:
            if check:
                res += game_num
    return res


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    cubes_count = {"red": 12, "green": 13, "blue": 14}

    part_1_ans = day_2(data, cubes_count, calculate_power=False)
    print(f"Part-1: {part_1_ans}")

    part_2_ans = day_2(data, cubes_count, calculate_power=True)
    print(f"Part-2: {part_2_ans}")


main()
