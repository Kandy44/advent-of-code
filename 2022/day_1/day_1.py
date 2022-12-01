def read_data():
    vals = [l.strip() for l in open("../inputs/1.in", "r")]
    elves_calorie_count = [
        sum(map(int, line.split("\n"))) for line in "\n".join(vals).split("\n\n")
    ]
    elves_calorie_count.sort(reverse=True)
    return elves_calorie_count


def first_n_max_calories_sum(calories, n=1):
    return sum(calories[:n])


def main():
    calories = read_data()
    print(first_n_max_calories_sum(calories, 1))
    print(first_n_max_calories_sum(calories, 3))


main()
