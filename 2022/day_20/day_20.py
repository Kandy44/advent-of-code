def read_data():
    with open("../inputs/20.in", "r") as fp:
        nums = [int(line.strip()) for line in fp]
        return nums


def update_lst(lst: list[tuple[int, int]], n: int, idx_val_pair: tuple[int, int]):
    pair_idx = lst.index(idx_val_pair)
    cur_pos_val = lst.pop(pair_idx)[0]
    updated_idx = (pair_idx + cur_pos_val) % (n - 1)
    lst.insert(updated_idx, idx_val_pair)


def grove_coordinates_sum(
    nums: list[int], coordinates: list[int], offset=1, repeat_op_count=1
):
    n = len(nums)
    nums = list(map(lambda x, offset=offset: x * offset, nums))
    nums_with_idxs = [(num, idx) for idx, num in enumerate(nums)]

    for _ in range(repeat_op_count):
        for idx, val in enumerate(nums):
            update_lst(nums_with_idxs, n, (val, idx))

    updated_nums = list(map(lambda x: x[0], nums_with_idxs))
    grove_sum = 0
    zero_idx = updated_nums.index(0)
    for coordinate in coordinates:
        grove_sum += updated_nums[(zero_idx + coordinate) % n]
    return grove_sum


def main():
    nums = read_data()
    coordinates = [1000, 2000, 3000]
    part_1_ans = grove_coordinates_sum(list(nums), coordinates)
    part_2_ans = grove_coordinates_sum(
        list(nums), coordinates, offset=811589153, repeat_op_count=10
    )
    print(part_1_ans)
    print(part_2_ans)


main()
