import sys
import re
from collections import Counter
from string import ascii_lowercase


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        row_regex = r"([^\d]+)(\d+)\[(.+)\]"
        rooms = []
        for line in fp.readlines():
            name, sector_id, checksum = re.findall(row_regex, line.strip("\n"))[0]
            sector_id = int(sector_id)
            rooms.append((name, sector_id, checksum))
        return rooms


def shift_char(ch, shift_num):
    chars = ascii_lowercase
    return chars[(chars.index(ch) + shift_num) % len(chars)]


def is_real_room(name, checksum):
    char_counter = Counter(name.replace("-", "")).most_common()
    char_counter.sort(key=lambda match: (-match[1], match[0]))
    most_common_chars = [match[0] for match in char_counter[:5]]
    return all(ch in checksum for ch in most_common_chars)


def part_1(rooms):
    sector_id_sum = 0
    for name, sector_id, checksum in rooms:
        if is_real_room(name, checksum):
            sector_id_sum += sector_id
    return sector_id_sum


def part_2(rooms):
    for name, sector_id, checksum in rooms:
        if is_real_room(name, checksum):
            for part in name.split("-"):
                decrypted_part = "".join(map(lambda x: shift_char(x, sector_id), part))
                if decrypted_part == "northpole":
                    return sector_id
    return 0


def main():
    filename = sys.argv[1]
    rooms = read_data(filename)

    part_1_ans = part_1(rooms)
    part_2_ans = part_2(rooms)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
