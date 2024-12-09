import sys


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return [line.strip("\n") for line in fp.readlines()]


def get_invalid_idxs(keypad):
    idxs = set()
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            if keypad[i][j] == ".":
                idxs.add((i, j))
    return idxs


def get_start_idx(keypad, start_char):
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            if keypad[i][j] == start_char:
                return (i, j)


def get_bathroom_code(instructions, keypad, start_char):
    start_num_idx = get_start_idx(keypad, start_char)
    bathroom_code = ""
    r, c = len(keypad), len(keypad)
    invalid_idxs = get_invalid_idxs(keypad)

    dirs = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

    for ins in instructions:
        for ch in ins:
            cur_dir = dirs[ch]
            tmp_x = start_num_idx[0] + cur_dir[0]
            tmp_y = start_num_idx[1] + cur_dir[1]
            if (0 <= tmp_x < r and 0 <= tmp_y < c) and (
                tmp_x,
                tmp_y,
            ) not in invalid_idxs:
                start_num_idx = (tmp_x, tmp_y)
        bathroom_code += keypad[start_num_idx[0]][start_num_idx[1]]
    return bathroom_code


def main():
    filename = sys.argv[1]
    instructions = read_data(filename)
    keypad_1 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    keypad_2 = [
        [".", ".", "1", ".", "."],
        [".", "2", "3", "4", "."],
        ["5", "6", "7", "8", "9"],
        [".", "A", "B", "C", "."],
        [".", ".", "D", ".", "."],
    ]

    part_1_ans = get_bathroom_code(instructions, keypad_1, "5")
    part_2_ans = get_bathroom_code(instructions, keypad_2, "5")
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
