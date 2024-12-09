import sys
import re


def find_seqs(s):
    hypernet_regex = r"\[(\w+)\]"
    hypernet_seqs = re.findall(hypernet_regex, s)
    s = re.sub(hypernet_regex, " ", s)
    supernet_seqs = s.split()
    return hypernet_seqs, supernet_seqs


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        data = []
        for line in fp.readlines():
            hypernet_seqs, supernet_seqs = find_seqs(line.strip("\n"))
            data.append((hypernet_seqs, supernet_seqs))
        return data


def is_valid_abba(s):
    for i in range(0, len(s) - 3):
        seq = s[i : i + 4]
        if len(set(seq)) == 2 and seq[:2][::-1] == seq[2:]:
            return True
    return False


def is_valid_ssl(hypernet_seqs, supernet_seqs):
    for s in supernet_seqs:
        for i in range(0, len(s) - 2):
            seq = s[i : i + 3]
            if seq[0] == seq[-1] and seq[0] != seq[1]:
                find_seq = seq[1] + seq[0] + seq[1]
                if any(find_seq in hypernet_seq for hypernet_seq in hypernet_seqs):
                    return True
    return False


def tls_support_count(data):
    count = 0
    for hypernet_seqs, supernet_seqs in data:
        is_valid_ip = all(not is_valid_abba(seq) for seq in hypernet_seqs)
        is_valid_ip = is_valid_ip and any(is_valid_abba(seq) for seq in supernet_seqs)
        if is_valid_ip:
            count += 1
    return count


def ssl_support_count(data):
    count = 0
    for hypernet_seqs, supernet_seqs in data:
        if is_valid_ssl(hypernet_seqs, supernet_seqs):
            count += 1
    return count


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    part_1_ans = tls_support_count(data)
    part_2_ans = ssl_support_count(data)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
