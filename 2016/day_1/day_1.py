import sys


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return "".join(line.strip("\n") for line in fp.readlines()).split(", ")


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def part_1(instructions):
    start_point = (0, 0)
    cur_point = (0, 0)

    cur_dir = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for ins in instructions:
        move_dir, val = ins[0], int(ins[1:])
        if move_dir == "L":
            cur_dir = (cur_dir - 1) % len(dirs)
        elif move_dir == "R":
            cur_dir = (cur_dir + 1) % len(dirs)

        cur_point = (
            cur_point[0] + dirs[cur_dir][0] * val,
            cur_point[1] + dirs[cur_dir][1] * val,
        )

        # print(cur_point)
    return dist(start_point, cur_point)


def part_2(instructions):
    start_point = (0, 0)
    cur_point = (0, 0)
    visited_idxs = set()

    cur_dir = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for ins in instructions:
        move_dir, val = ins[0], int(ins[1:])
        if move_dir == "L":
            cur_dir = (cur_dir - 1) % len(dirs)
        elif move_dir == "R":
            cur_dir = (cur_dir + 1) % len(dirs)

        for _ in range(val):
            cur_point = (
                cur_point[0] + dirs[cur_dir][0],
                cur_point[1] + dirs[cur_dir][1],
            )

            if cur_point in visited_idxs:
                return dist(start_point, cur_point)

            visited_idxs.add(cur_point)
    return 0


def main():
    filename = sys.argv[1]
    instructions = read_data(filename)
    part_1_ans = part_1(instructions)
    part_2_ans = part_2(instructions)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
