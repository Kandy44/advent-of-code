import sys
import copy


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return list(map(int, "".join(line.strip("\n") for line in fp.readlines())))


def part_1(data):
    if len(data) % 2 != 0:
        data.append(0)
    blocks = []

    cur_idx = 0

    for i, j in zip(data[0::2], data[1::2]):
        blocks.extend([cur_idx for _ in range(i)] + ["." for _ in range(j)])
        cur_idx += 1

    n = len(blocks)
    empty_idxs = [i for i in range(n) if blocks[i] == "."]
    non_empty_idxs = [i for i in range(n - 1, -1, -1) if blocks[i] != "."]

    for empty_idx, non_empty_idx in zip(empty_idxs, non_empty_idxs):
        blocks[empty_idx], blocks[non_empty_idx] = (
            blocks[non_empty_idx],
            blocks[empty_idx],
        )

        first_empty_idx = blocks.index(".")
        if any(blocks[i] != "." for i in range(first_empty_idx, n)):
            continue
        else:
            break
    checksum = sum(int(ch) * i for i, ch in enumerate(blocks) if ch != ".")
    return checksum


def part_2(data):
    if len(data) % 2 != 0:
        data.append(0)

    blocks = []
    cur_idx = 0
    d = {}

    for i, j in zip(data[0::2], data[1::2]):
        blocks.extend([cur_idx for _ in range(i)] + ["." for _ in range(j)])
        d[cur_idx] = i
        cur_idx += 1

    for i in range(cur_idx - 1, -1, -1):
        search_str = ["." for _ in range(d[i])]

        l1 = next(
            (
                j
                for j in range(0, len(blocks) - d[i] - 1)
                if blocks[j : j + d[i]] == search_str
            ),
            -1,
        )

        if l1 != -1:
            r1 = l1 + d[i]
            l2 = blocks.index(i)
            r2 = l2 + d[i]

            if l1 < l2 and r1 < r2:
                blocks[l1:r1], blocks[l2:r2] = blocks[l2:r2], blocks[l1:r1]
    return sum(ch * i for i, ch in enumerate(blocks) if ch != ".")


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    part_1_ans = part_1(copy.deepcopy(data))
    part_2_ans = part_2(copy.deepcopy(data))
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
