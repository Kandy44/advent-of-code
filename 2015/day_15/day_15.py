import sys
import re
from itertools import product

INGREDIENTS_REG = r"(.+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"


def solve_day_15(data, total_amount, total_calories):
    ingredients = []
    for row in data:
        name, capacity, durability, flavor, texture, calories = re.findall(
            INGREDIENTS_REG, row
        )[0]
        capacity, durability, flavor, texture, calories = map(
            int, [capacity, durability, flavor, texture, calories]
        )
        ingredients.append((name, capacity, durability, flavor, texture, calories))

    max_score = 0
    best_calories = 0

    for comb in product(range(0, total_amount + 1), repeat=4):
        if sum(comb) == total_amount:
            cap_sum, dur_sum, flav_sum, tex_sum, cal_sum = 0, 0, 0, 0, 0

            for cur_ing, teaspoons in zip(ingredients, comb):
                cap_sum += cur_ing[1] * teaspoons
                dur_sum += cur_ing[2] * teaspoons
                flav_sum += cur_ing[3] * teaspoons
                tex_sum += cur_ing[4] * teaspoons
                cal_sum += cur_ing[5] * teaspoons

            if cap_sum <= 0 or dur_sum <= 0 or flav_sum <= 0:
                continue

            cur_score = cap_sum * dur_sum * flav_sum * tex_sum
            if cal_sum == total_calories:
                best_calories = max(best_calories, cur_score)
            max_score = max(max_score, cur_score)
    return (max_score, best_calories)


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = [line.strip("\n") for line in fp.readlines()]
        return lines


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    total_amount = 100
    total_calories = 500

    part_1_ans, part_2_ans = solve_day_15(data, total_amount, total_calories)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
