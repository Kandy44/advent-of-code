import hashlib


def get_data():
    with open("../inputs/4.in", "r") as fp:
        return fp.readline().strip("\n")


def get_hash(key):
    res = hashlib.md5(key.encode())
    return res.hexdigest()


def get_lowest_pos_num(secret_key, zeros, start_num=0):
    prefix_check = "0" * zeros
    while True:
        cur_hash = get_hash(secret_key + str(start_num))
        if cur_hash.startswith(prefix_check):
            return start_num
        start_num += 1


def main():
    secret_key = get_data()
    part_1_ans = get_lowest_pos_num(secret_key, zeros=5, start_num=0)
    part_2_ans = get_lowest_pos_num(secret_key, zeros=6, start_num=part_1_ans)
    print(part_1_ans)
    print(part_2_ans)


main()
