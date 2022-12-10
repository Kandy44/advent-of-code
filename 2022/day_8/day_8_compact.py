def read_data():
    with open("../inputs/8.in", "r") as fp:
        return [list(map(int,list(line.strip('\n')))) for line in fp]

def check_all_directions(grid,i,j):
    cur_val = grid[i][j]
    dirs = [[j - 1, -1, -1],[j + 1, len(grid[i])],[i - 1, -1, -1],[i+1,len(grid[0])]]
    cur_tree_score = 1
    any_dir_possible = False    
    for dir_num,dir_idx in enumerate(range(len(dirs))):
        cur_dir_score = 0
        cur_dir_possible = True
        for k in range(*dirs[dir_idx]):
            cur_dir_score += 1
            cur_grid_val = grid[i][k] if dir_num == 0 or dir_num == 1 else grid[k][j]
            if cur_grid_val >= cur_val:
                cur_dir_possible = False
                break
        cur_tree_score *= cur_dir_score
        any_dir_possible = any_dir_possible or cur_dir_possible
    return (any_dir_possible,cur_tree_score)

def get_tree_info(data):
    count = 0
    max_score = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            res = check_all_directions(data,i,j)
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
