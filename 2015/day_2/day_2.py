from math import prod


def get_data():
    with open("../inputs/2.in", "r") as fp:
        return [sorted(list(map(int, line.strip("\n").split("x")))) for line in fp]


def get_surface_area(l, w, h):
    sides = [2 * l * w, 2 * w * h, 2 * h * l]
    return sum(sides) + (min(sides) // 2)


def get_feet(dims, ribbon=False):
    total_feet = 0
    for dim in dims:
        if ribbon:
            total_feet += (sum(dim[:2]) * 2) + (prod(dim))
        else:
            total_feet += get_surface_area(*dim)
    return total_feet


def main():
    dims = get_data()
    print(get_feet(dims, ribbon=False))
    print(get_feet(dims, ribbon=True))


main()
