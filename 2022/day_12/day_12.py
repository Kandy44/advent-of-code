def read_map() -> list[list]:
    grid = []
    start_idxs = None
    end_idxs = None
    with open("../inputs/12.in", "r") as fp:
        i = 0
        for line in fp:
            row = list(line.strip('\n'))
            if 'S' in row:
                start_idxs = (i, row.index('S'))
                row[start_idxs[1]] = 'a'
            if 'E' in row:
                end_idxs = (i, row.index('E'))
                row[end_idxs[1]] = 'z'
            grid.append(row)
            i+=1
    return [grid, start_idxs, end_idxs]


def get_min_steps(grid, start_idxs, end_idxs,is_hiking_trail=False) -> int:
    q = []
    visited_points = set()
    
    if is_hiking_trail:
        q.append((0, end_idxs[0], end_idxs[1]))
        visited_points.add(end_idxs)
    else:
        q.append((0, start_idxs[0], start_idxs[1]))
        visited_points.add(start_idxs) 
    
    while q:
        dist, r, c = q.pop(0)
        for dx, dy in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if not ((0 <= dx < len(grid)) and (0 <= dy < len(grid[0]))):
                continue
            elif (dx, dy) in visited_points:
                    continue
            
            square_diff = ord(grid[dx][dy])-ord(grid[r][c])

            if is_hiking_trail:
                if square_diff < -1:
                    continue
                elif grid[dx][dy] == "a":
                    return dist+1
            else:
                if square_diff > 1:
                    continue
                elif (dx, dy) == end_idxs:
                    return dist+1
            visited_points.add((dx, dy))
            q.append((dist + 1, dx, dy))

def main():
    grid, start_idxs, end_idxs = read_map()
    print(get_min_steps(grid, start_idxs, end_idxs,is_hiking_trail=False))
    print(get_min_steps(grid, start_idxs, end_idxs,is_hiking_trail=True))


main()
