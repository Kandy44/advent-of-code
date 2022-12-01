import numpy as np

grid_size = (1000, 1000)


def get_data():
    with open("../inputs/6.in", "r") as fp:
        return [line.strip("\n").split(" ") for line in fp]


def total_brightness(instructions, toggle_increment=False):
    grid = np.zeros(grid_size, "int32")

    for ins in instructions:
        x1, y1 = map(int, ins[-3].split(","))
        x2, y2 = map(int, ins[-1].split(","))
        if ins[-4] == "on":
            if toggle_increment:
                grid[x1 : x2 + 1, y1 : y2 + 1] += 1
            else:
                grid[x1 : x2 + 1, y1 : y2 + 1] = 1
        elif ins[-4] == "off":
            if toggle_increment:
                grid[x1 : x2 + 1, y1 : y2 + 1] -= 1
                grid[grid < 0] = 0
            else:
                grid[x1 : x2 + 1, y1 : y2 + 1] = 0

        elif ins[-4] == "toggle":
            if toggle_increment:
                grid[x1 : x2 + 1, y1 : y2 + 1] += 2
            else:
                grid[x1 : x2 + 1, y1 : y2 + 1] = np.logical_not(
                    grid[x1 : x2 + 1, y1 : y2 + 1]
                )
    return np.sum(grid)


def main():
    instructions = get_data()
    print(total_brightness(instructions, toggle_increment=False))
    print(total_brightness(instructions, toggle_increment=True))


main()
