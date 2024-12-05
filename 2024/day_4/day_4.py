import sys


def part_1(grid, WORD):
    count = 0
    WORD_BOUND_IDX = len(WORD) - 1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != WORD[0]:
                continue
            for x_dir in [-1, 0, 1]:
                for y_dir in [-1, 0, 1]:
                    if x_dir == 0 and y_dir == 0:
                        continue
                    if not (
                        0 <= r + WORD_BOUND_IDX * x_dir < len(grid)
                        and 0 <= c + WORD_BOUND_IDX * y_dir < len(grid[0])
                    ):
                        continue
                    if all(
                        grid[r + offset * x_dir][c + offset * y_dir] == WORD[offset]
                        for offset in range(1, len(WORD))
                    ):
                        count += 1
    return count


def part_2(data):
    count = 0
    valid_corners = ["MMSS", "MSSM", "SMMS", "SSMM"]
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if data[i][j] != "A":
                continue
            corners = "".join(
                [
                    data[i - 1][j - 1],
                    data[i - 1][j + 1],
                    data[i + 1][j + 1],
                    data[i + 1][j - 1],
                ]
            )
            count += corners in valid_corners
    return count


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return [list(row.strip("\n")) for row in fp.readlines()]


def main():
    filename = sys.argv[1]
    WORD = "XMAS"
    data = read_data(filename)
    part_1_ans, part_2_ans = part_1(data, WORD), part_2(data)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
