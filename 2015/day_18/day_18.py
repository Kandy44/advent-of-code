import copy
import sys


def part_1(grid, total_steps):
    for _ in range(total_steps):
        f = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                count = 0
                idxs = [
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j - 1),
                    (i, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j),
                    (i + 1, j + 1),
                ]

                for x, y in idxs:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if grid[x][y] == "#":
                            count += 1

                if grid[i][j] == "#":
                    if count < 2 or count > 3:
                        f[(i, j)] = "."
                else:
                    if count == 3:
                        f[(i, j)] = "#"

        for (i, j), val in f.items():
            grid[i][j] = val

    return sum(row.count("#") for row in grid)


def part_2(grid, total_steps):
    skip_idxs = [
        (0, 0),
        (0, len(grid) - 1),
        (len(grid) - 1, 0),
        (len(grid) - 1, len(grid[0]) - 1),
    ]

    for x, y in skip_idxs:
        grid[x][y] = "#"

    for _ in range(total_steps):
        f = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                if (i, j) in skip_idxs:
                    continue

                count = 0
                idxs = [
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j - 1),
                    (i, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j),
                    (i + 1, j + 1),
                ]

                for x, y in idxs:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if grid[x][y] == "#":
                            count += 1

                if grid[i][j] == "#":
                    if count < 2 or count > 3:
                        f[(i, j)] = "."
                else:
                    if count == 3:
                        f[(i, j)] = "#"

        for (i, j), val in f.items():
            grid[i][j] = val

    return sum(row.count("#") for row in grid)


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        grid = [list(line.strip("\n")) for line in fp.readlines()]
        return grid


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    STEPS_COUNT = 100

    part_1_ans, part_2_ans = (
        part_1(copy.deepcopy(data), STEPS_COUNT),
        part_2(copy.deepcopy(data), STEPS_COUNT),
    )
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
