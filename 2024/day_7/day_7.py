import sys

sys.setrecursionlimit(10**6)


def is_valid_equation(nums, cur_val, target_val, cur_idx, use_concat_op):
    if cur_idx == len(nums):
        return cur_val == target_val

    if is_valid_equation(
        nums, cur_val + nums[cur_idx], target_val, cur_idx + 1, use_concat_op
    ):
        return True
    elif is_valid_equation(
        nums, cur_val * nums[cur_idx], target_val, cur_idx + 1, use_concat_op
    ):
        return True
    elif use_concat_op and is_valid_equation(
        nums,
        int(str(cur_val) + str(nums[cur_idx])),
        target_val,
        cur_idx + 1,
        use_concat_op,
    ):
        return True
    return False


def solve_equations(data):
    part_1_ans, part_2_ans = 0, 0
    for row in data:
        target_val, *nums = row
        if is_valid_equation(nums, nums[0], target_val, 1, False):
            part_1_ans += target_val
        if is_valid_equation(nums, nums[0], target_val, 1, True):
            part_2_ans += target_val
    return (part_1_ans, part_2_ans)


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = []
        for line in fp.readlines():
            nums = line.strip("\n").replace(":", " ").split()
            nums = list(map(int, nums))
            lines.append(nums)

        return lines


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    part_1_ans, part_2_ans = solve_equations(data)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
