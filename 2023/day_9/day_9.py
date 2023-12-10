# Part-1: 1806615041
# Part-2: 1211
import sys


def read_data(filename):
    rows = []
    with open(filename, "r", encoding="utf-8") as fp:
        rows = [list(map(int, row.split(" "))) for row in fp.readlines()]
    return rows


def get_prediction(lst, add_index):
    if lst.count(0) == len(lst):
        return 0
    new_lst = [lst[i + 1] - lst[i] for i in range(0, len(lst) - 1)]
    # Add new prediction if add_index is -1 else subtract
    return lst[add_index] + (get_prediction(new_lst, add_index) * [-1, 1][add_index])


def day_9(rows):
    return (sum(get_prediction(row, idx) for row in rows) for idx in [-1, 0])


def main():
    filename = sys.argv[1]
    rows = read_data(filename)
    part_1_ans, part_2_ans = day_9(rows)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
