import sys

MOVE_DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def is_inf_loop(grid, s_x, s_y):
    visited_idxs = set()
    guard_dir = 0

    while True:
        visited_idxs.add((s_x, s_y, guard_dir))
        new_s_x, new_s_y = s_x + MOVE_DIRS[guard_dir][0], s_y + MOVE_DIRS[guard_dir][1]
        if not (0 <= new_s_x < len(grid) and 0 <= new_s_y < len(grid[0])):
            return False

        if grid[new_s_x][new_s_y] == "#":
            guard_dir = (guard_dir + 1) % len(MOVE_DIRS)
        else:
            s_x, s_y = new_s_x, new_s_y

        if (s_x, s_y, guard_dir) in visited_idxs:
            return True


def part_1(grid, start_idx):
    s_x, s_y = start_idx
    visited_idxs = set()

    guard_dir = 0

    while True:
        visited_idxs.add((s_x, s_y))
        new_s_x, new_s_y = s_x + MOVE_DIRS[guard_dir][0], s_y + MOVE_DIRS[guard_dir][1]
        if not (0 <= new_s_x < len(grid) and 0 <= new_s_y < len(grid[0])):
            break

        if grid[new_s_x][new_s_y] == "#":
            guard_dir = (guard_dir + 1) % len(MOVE_DIRS)
        else:
            s_x, s_y = new_s_x, new_s_y

    return visited_idxs, len(visited_idxs)


def part_2(grid, visited_idxs, start_idx):
    # Placing the obstacles on the indexes where the guard has already visited will decrease the iterations,
    # compared to modifiying every possible index
    s_x, s_y = start_idx
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                continue

            if (i, j) in visited_idxs:
                grid[i][j] = "#"
                if is_inf_loop(grid, s_x, s_y):
                    count += 1
                grid[i][j] = "."
    return count


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = []
        start_idx = (-1, -1)
        for line_idx, line in enumerate(fp.readlines()):
            row = list(line.strip("\n"))
            if "^" in row:
                start_idx = (line_idx, row.index("^"))
            lines.append(row)
        return [lines, start_idx]


def main():
    filename = sys.argv[1]
    data, start_idx = read_data(filename)
    visited_idxs, part_1_ans = part_1(data, start_idx)
    part_2_ans = part_2(data, visited_idxs, start_idx)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
