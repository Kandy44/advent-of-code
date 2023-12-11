# Part-1: 9445168
# Part-2: 742305960572
import sys


def read_data(filename: str) -> list[list[list[int, int]], list[int], list[int]]:
    galaxy_idxs: list[list[int, int]] = []
    with open(filename, "r", encoding="utf-8") as fp:
        rows = [line.strip("\n") for line in fp.readlines()]
        for row_idx, line in enumerate(rows):
            for col_idx, ch in enumerate(line):
                if ch == "#":
                    galaxy_idxs.append((row_idx, col_idx))

    empty_row_idxs = [i for i, row in enumerate(rows) if row.count(".") == len(row)]
    empty_col_idxs = [i for i, col in enumerate(zip(*rows)) if col.count(".") == len(col)]
    empty_row_idxs.sort(reverse=True)
    empty_col_idxs.sort(reverse=True)
    return (galaxy_idxs, empty_row_idxs, empty_col_idxs)


def dist(p1: list[int], p2: list[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def sum_of_shortest_paths(
    galaxy_idxs: list[list[int, int]],
    empty_row_idxs: list[int],
    empty_col_idxs: list[int],
    offset: int,
) -> int:
    for row_idx in empty_row_idxs:
        galaxy_idxs = [(x + offset if x > row_idx else x, y) for (x, y) in galaxy_idxs]
    for col_idx in empty_col_idxs:
        galaxy_idxs = [(x, y + offset if y > col_idx else y) for (x, y) in galaxy_idxs]
    res = 0
    for idx, galaxy_idx_1 in enumerate(galaxy_idxs):
        for galaxy_idx_2 in galaxy_idxs[idx + 1 :]:
            res += dist(galaxy_idx_1, galaxy_idx_2)
    return res


def day_11(
    galaxy_idxs: list[list[int, int]],
    empty_row_idxs: list[int],
    empty_col_idxs: list[int],
    offsets: list[int],
) -> list[int]:
    return (sum_of_shortest_paths(galaxy_idxs, empty_row_idxs, empty_col_idxs, offset - 1) for offset in offsets)


def main():
    filename = sys.argv[1]
    galaxy_idxs, empty_row_idxs, empty_col_idxs = read_data(filename)
    part_1_ans, part_2_ans = day_11(
        galaxy_idxs, empty_row_idxs, empty_col_idxs, [2, 1000000]
    )
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
