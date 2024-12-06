import sys


def day_23(instructions, reg):
    cur_idx = 0
    while cur_idx < len(instructions):
        if instructions[cur_idx].startswith("hlf"):
            _, reg_name = instructions[cur_idx].split(" ")
            reg_name = reg_name.strip()
            reg[reg_name] //= 2
            cur_idx += 1
        elif instructions[cur_idx].startswith("tpl"):
            _, reg_name = instructions[cur_idx].split(" ")
            reg_name = reg_name.strip()
            reg[reg_name] *= 3
            cur_idx += 1
        elif instructions[cur_idx].startswith("inc"):
            _, reg_name = instructions[cur_idx].split(" ")
            reg_name = reg_name.strip()
            reg[reg_name] += 1
            cur_idx += 1
        elif instructions[cur_idx].startswith("jmp"):
            _, offset = instructions[cur_idx].split(" ")
            offset = int(offset)
            cur_idx += offset

        elif instructions[cur_idx].startswith("jie"):
            reg_name, offset = instructions[cur_idx][3:].split(",")
            reg_name = reg_name.strip()
            offset = int(offset.strip())
            if reg[reg_name] % 2 == 0:
                cur_idx += offset
            else:
                cur_idx += 1
        elif instructions[cur_idx].startswith("jio"):
            reg_name, offset = instructions[cur_idx][3:].split(",")
            reg_name = reg_name.strip()
            offset = int(offset.strip())
            if reg[reg_name] == 1:
                cur_idx += offset
            else:
                cur_idx += 1

    return reg["b"]


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        instructions = [line.strip("\n") for line in fp.readlines()]
        return instructions


def main():
    filename = sys.argv[1]
    instructions = read_data(filename)
    reg1 = {"a": 0, "b": 0}
    reg2 = {"a": 1, "b": 0}

    part_1_ans, part_2_ans = (
        day_23(instructions, reg1),
        day_23(instructions, reg2),
    )
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
