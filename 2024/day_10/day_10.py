import sys
from collections import deque


def in_range(n, m, x, y):
    return (0 <= x < n) and (0 <= y < m)


def get_final_idxs(grid, zero_idx):
    n, m = len(grid), len(grid[0])
    r, c = zero_idx
    q = deque([(r, c)])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited_idxs = []

    while len(q) > 0:
        r, c = q.popleft()
        if grid[r][c] == 9:
            visited_idxs.append((r, c))
            continue
        for x, y in dirs:
            new_r, new_c = r + x, c + y
            # If index is in bounds, get the char.
            # Else If index is out of bounds, then make the number to be checked as 0.
            check_val = grid[new_r][new_c] if in_range(n, m, new_r, new_c) else 0
            if check_val == (grid[r][c] + 1):
                q.append((new_r, new_c))
    return visited_idxs


def day_10(grid, zero_idxs):
    part_1_ans, part_2_ans = 0, 0
    for zero_idx in zero_idxs:
        final_idxs = get_final_idxs(grid, zero_idx)
        part_1_ans += len(set(final_idxs))
        part_2_ans += len(final_idxs)

    return (part_1_ans, part_2_ans)


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        grid = []
        zero_idxs = []
        for row_idx, line in enumerate(fp.readlines()):
            row = [ch if ch == "." else int(ch) for ch in line.strip("\n")]
            grid.append(row)
            for col_idx, ch in enumerate(row):
                if ch == 0:
                    zero_idxs.append((row_idx, col_idx))
        return [grid, zero_idxs]


def main():
    filename = sys.argv[1]
    grid, zero_idxs = read_data(filename)
    part_1_ans, part_2_ans = day_10(grid, zero_idxs)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
