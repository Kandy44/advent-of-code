import sys
import hashlib


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return "".join([line for line in fp.readlines()])


def is_valid_hash(door_id, num, start_str):
    s = door_id + str(num)
    s_hash = hashlib.md5(s.encode("utf-8")).hexdigest()
    is_valid = s_hash.startswith(start_str)
    return (s_hash, is_valid)


def part_1(door_id, password_length, start_str):
    start_num = 0
    password = ""

    while len(password) != password_length:
        s_hash, is_valid = is_valid_hash(door_id, start_num, start_str)
        if is_valid:
            password += s_hash[5]
        start_num += 1
    return password


def part_2(door_id, password_length, start_str):
    start_num = 0
    password = ["_" for _ in range(password_length)]
    filled_positions = password_length

    while filled_positions > 0:
        s_hash, is_valid = is_valid_hash(door_id, start_num, start_str)
        idx = int(s_hash[5]) if s_hash[5] in "01234567" else -1
        if is_valid and idx != -1 and password[idx] == "_":
            password[idx] = s_hash[6]
            filled_positions -= 1
        start_num += 1
    return "".join(password)


def main():
    filename = sys.argv[1]
    door_id = read_data(filename)
    password_length = 8
    start_str = "0" * 5
    part_1_ans = part_1(door_id, password_length, start_str)
    part_2_ans = part_2(door_id, password_length, start_str)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
