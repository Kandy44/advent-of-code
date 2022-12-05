def stack_count():
    with open('../inputs/5.in') as fp:
        for line in fp:
            if all(i.strip().isdigit() for i in line.strip().split('  ')):
                return len(line.strip().split('  '))

def read_data():
    with open('../inputs/5.in') as fp:
        stacks = [[] for _ in range(stack_count())]
        operations = []
        for line in fp:
            if any(i.isdigit() for i in line) and line.count('move') == 0:
                continue
            elif line.count('move') > 0:
                operations.append(line.strip('\n').split(' '))
            else:
                i = 0
                parts = line.strip('\n').split('    ')
                for part in parts:
                    if part == '':
                        stacks[i].append(part)
                        i += 1
                    else:
                        for val in part.split(' '):
                            # Removing brackets around crate name
                            stacks[i].append(val[1:-1])
                            i += 1

        stacks = [[val for val in row if val != ''] for row in stacks]
        return stacks,operations

def find_top_crates(stacks,operations,reverse_crates=False):
    for op in operations:
        count,from_idx,to_idx = map(int,[op[1],op[3],op[5]])
        from_idx,to_idx = from_idx-1,to_idx-1
        movable_crates = stacks[from_idx][:count]
        
        if isinstance(movable_crates,int):
            movable_crates = [movable_crates]
        if reverse_crates:
            movable_crates = movable_crates[::-1]
        
        stacks[to_idx] = movable_crates + stacks[to_idx]
        stacks[from_idx] = stacks[from_idx][count:]
    return ''.join(row[0] for row in stacks)


def main():
    stacks,operations = read_data()
    print(find_top_crates(list(stacks),operations,reverse_crates=True))
    print(find_top_crates(list(stacks),operations,reverse_crates=False))
main()