import string
import sys


def get_password(n):
    name = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        name = chr(r + ord("a")) + name
    return name


def get_password_num(s):
    n = 0
    for c in s:
        n = n * 26 + 1 + ord(c) - ord("a")
    return n


def is_valid_password(s):
    if any(ch in s for ch in "iol"):
        return False
    if sum([s.count(ch * 2) for ch in string.ascii_lowercase]) < 2:
        return False

    for i in range(0, len(s) - 2):
        a, b, c = s[i : i + 3]
        diff1, diff2 = ord(b) - ord(a) == 1, ord(c) - ord(b) == 1
        if diff1 == 1 and diff2 == 1:
            return True
    return False


def day_10(password, passwords_required):
    passwords = []
    password_num = get_password_num(password)

    while passwords_required > 0:
        if is_valid_password(password):
            passwords.append(password)
            passwords_required -= 1
        password = get_password(password_num)
        password_num += 1

    return passwords


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return "".join([line.strip("\n") for line in fp.readlines()])


def main():
    filename = sys.argv[1]
    password = read_data(filename)
    passwords_required = 2
    part_1_ans, part_2_ans = day_10(password, passwords_required)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
