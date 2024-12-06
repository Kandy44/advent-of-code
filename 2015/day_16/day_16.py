import sys


def part_1(data, helper_info):
    aunts = []
    for aunt in data:
        first_sp, first_colon = aunt.index(" "), aunt.index(":")
        aunt_num = int(aunt[first_sp:first_colon])
        aunt_things = aunt[len("Sue ") + (first_colon - first_sp) :].strip().split(", ")
        aunt_cond_check = sum(thing in helper_info for thing in aunt_things)
        aunts.append((aunt_num, aunt_cond_check))

    aunts.sort(key=lambda x: x[1], reverse=True)
    aunt_num = aunts[0][0]
    return aunt_num


def part_2(data, helper_info):
    aunts = []
    for aunt in data:
        first_sp, first_colon = aunt.index(" "), aunt.index(":")
        aunt_num = int(aunt[first_sp:first_colon])
        aunt_things = aunt[len("Sue ") + (first_colon - first_sp) :].strip().split(", ")

        aunt_cond_check = 0

        for thing in helper_info:
            req_thing, count = thing.split(": ")
            count = int(count.strip())
            for aunt_thing in aunt_things:
                if req_thing in aunt_thing:
                    _, thing_count = aunt_thing.split(": ")
                    thing_count = int(thing_count.strip())

                    if req_thing in ["cats", "trees"]:
                        if thing_count > count:
                            aunt_cond_check += 1
                    if req_thing in ["pomeranians", "goldfish"]:
                        if thing_count < count:
                            aunt_cond_check += 1
                    else:
                        aunt_cond_check += thing == aunt_thing
        aunts.append((aunt_num, aunt_cond_check))

    aunts.sort(key=lambda x: x[1], reverse=True)
    aunt_num = aunts[0][0]
    return aunt_num


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        lines = [line.strip("\n") for line in fp.readlines()]
        return lines


def main():
    helper_info = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split("\n")
    filename = sys.argv[1]
    data = read_data(filename)

    part_1_ans, part_2_ans = part_1(data, helper_info), part_2(data, helper_info)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
