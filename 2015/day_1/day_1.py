basement = -1


def get_data():
    with open("../inputs/1.in", "r") as fp:
        return fp.readline().strip("\n")


def get_floor_details(instructions, get_basement=False):
    current_floor = 0
    current_pos = 0
    for ins in instructions:
        if current_floor == basement and get_basement:
            return current_pos
        if ins == "(":
            current_floor += 1
        elif ins == ")":
            current_floor -= 1
        current_pos += 1
    return current_floor


def main():
    instructions = get_data()
    print(get_floor_details(instructions,get_basement=False))
    print(get_floor_details(instructions, get_basement=True))


main()
