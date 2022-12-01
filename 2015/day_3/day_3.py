def get_data():
    with open("../inputs/3.in", "r") as fp:
        return fp.readline().strip("\n")


def get_new_direction(direction, cur_x, cur_y):
    if direction == "^":
        return (cur_x + 1, cur_y)
    elif direction == "v":
        return (cur_x - 1, cur_y)
    elif direction == ">":
        return (cur_x, cur_y + 1)
    elif direction == "<":
        return (cur_x, cur_y - 1)


def houses_with_presents(directions, robot=False):
    visited_houses = set()
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    visited_houses.add((santa_x, santa_y))
    can_robot_move = False

    if robot:
        visited_houses.add((robo_x, robo_y))

    for direction in directions:
        if robot:
            if not can_robot_move:
                santa_x, santa_y = get_new_direction(direction, santa_x, santa_y)
                visited_houses.add((santa_x, santa_y))
            else:
                robo_x, robo_y = get_new_direction(direction, robo_x, robo_y)
                visited_houses.add((robo_x, robo_y))
            can_robot_move = not can_robot_move
        else:
            santa_x, santa_y = get_new_direction(direction, santa_x, santa_y)
            visited_houses.add((santa_x, santa_y))

    return len(visited_houses)


def main():
    directions = get_data()
    print(houses_with_presents(directions, robot=False))
    print(houses_with_presents(directions, robot=True))


main()
