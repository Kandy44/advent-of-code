def read_data():
    with open("../inputs/8.in", "r") as fp:
        return [list(map(int,list(line.strip('\n')))) for line in fp]

def check_left(grid, cur_val, i, j):
    c = 0
    for k in range(j - 1, -1, -1):
        c += 1
        if grid[i][k] >= cur_val:
            return (False, c)
    return (True, c)


def check_right(grid, cur_val, i, j):
    c = 0
    for k in range(j + 1, len(grid[i])):
        c += 1
        if grid[i][k] >= cur_val:
            return (False, c)
    return (True, c)


def check_top(grid, cur_val, i, j):
    c = 0
    for k in range(i - 1, -1, -1):
        c += 1
        if grid[k][j] >= cur_val:
            return (False, c)
    return (True, c)


def check_bottom(grid, cur_val, i, j):
    c = 0
    for k in range(i + 1, len(grid[0])):
        c += 1
        if grid[k][j] >= cur_val:
            return (False, c)
    return (True, c)

def can_be_found(grid, i, j):
    cur_val = grid[i][j]
    directions_fun = [check_left,check_right,check_top,check_bottom]
    all_directions_count = [directions_fun[k](grid,cur_val,i,j) for k in range(len(directions_fun))]
    cur_score = 1
    any_dir_possible = False
    for (is_visible,dir_count) in all_directions_count:
        cur_score *= dir_count
        any_dir_possible = any_dir_possible or is_visible
    return (any_dir_possible,cur_score)

def get_tree_info(data):
    count = 0
    max_score = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            res = can_be_found(data, i, j)
            max_score = max(max_score, res[1])
            if res[0]:
                count += 1
    return (count,max_score)

def main():
    data = read_data()
    part_1,part_2 = get_tree_info(data)
    print(part_1)
    print(part_2)

main()
