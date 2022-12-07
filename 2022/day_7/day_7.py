DIR_SIZE_LIMIT = 100000
FREE_SPACE_REQUIRED = 30000000
FILESYSTEM_SIZE = 70000000


def read_data():
    with open("../inputs/7.in", "r") as fp:
        return [line.strip('\n') for line in fp]


def dir_sum(dir_contents, cur_dir):
    cur_sum = 0
    cur_dir_contents = dir_contents[cur_dir]
    for cur_entry in cur_dir_contents:
        if isinstance(cur_entry, list):
            cur_sum += int(cur_entry[0])
        else:
            if cur_dir == '/':
                cur_sum += dir_sum(dir_contents, cur_dir + cur_entry)
            else:
                cur_sum += dir_sum(dir_contents, cur_dir + '/' + cur_entry)
    return cur_sum


def get_dir_path(dir_lst):
    return dir_lst[0] + '/'.join(dir_lst[1:])


def get_dir_details(data):
    current_dir = []
    i = 0
    dir_contents = {}
    while i < len(data):
        line_parts = data[i].split(' ')
        i += 1
        if line_parts[1] == 'cd':
            if line_parts[-1] == '/':
                current_dir = ['/']
            elif line_parts[-1] == '..':
                current_dir.pop()
            else:
                current_dir.append(line_parts[-1])

        elif line_parts[1] == 'ls':
            while i < len(data) and '$' not in data[i]:
                line_parts = data[i].split(' ')
                current_dir_path = get_dir_path(current_dir)
                if 'dir' not in data[i]:
                    dir_contents[current_dir_path] = dir_contents.get(
                        current_dir_path, []) + [line_parts]
                else:
                    dir_contents[current_dir_path] = dir_contents.get(
                        current_dir_path, []) + [line_parts[-1]]
                i += 1

    root_space = dir_sum(dir_contents, '/')
    rem_space = FILESYSTEM_SIZE - root_space
    atleast_min_spaces = []

    dir_sizes_sum = 0
    for i in dir_contents.keys():
        if i != '/':
            cur_dir_sum = dir_sum(dir_contents, i)
            if cur_dir_sum <= DIR_SIZE_LIMIT:
                dir_sizes_sum += cur_dir_sum
            if cur_dir_sum + rem_space >= FREE_SPACE_REQUIRED:
                atleast_min_spaces.append(cur_dir_sum)
    return (dir_sizes_sum, min(atleast_min_spaces))


def main():
    data = read_data()
    part_1, part_2 = get_dir_details(data)
    print(part_1)
    print(part_2)


main()
