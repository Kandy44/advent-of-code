def get_data():
    with open("../inputs/5.in", "r") as fp:
        return [line.strip("\n") for line in fp]


def nice_string_orig(s):
    if any(word in s for word in ["ab", "cd", "pq", "xy"]):
        return 0
    if sum(ch in "aeiou" for ch in s) < 3:
        return 0

    if not any(s[i] == s[i + 1] for i in range(0, len(s) - 1)):
        return 0
    return 1


def nice_string_updated(s):
    check1 = any(s.count(s[i : i + 2]) >= 2 for i in range(0, len(s) - 1))
    check2 = any(s[i] == s[i + 2] for i in range(0, len(s) - 2))

    return check1 and check2


def count_nice_strings(strings, updated=False):
    count = 0
    for string in strings:
        count += nice_string_updated(string) if updated else nice_string_orig(string)
    return count


def main():
    strings = get_data()
    print(count_nice_strings(strings, updated=False))
    print(count_nice_strings(strings, updated=True))

    # print(nice_string_updated("aaa"))

    # print(nice_string_updated("xyxy"))

    # print(nice_string_updated("qjhvhtzxzqqjkmpb"))
    # print(nice_string_updated("xxyxx"))
    # print(nice_string_updated("uurcxstgmygtbstg"))
    # print(nice_string_updated("ieodomkazucvgmuy"))


main()
