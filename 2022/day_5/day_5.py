def read_data():
    with open('../inputs/5.in') as fp:
        stacks = []
        operations = []
        for line in fp:
            if line.count('move') > 0:
                operations.append(line.strip('\n').split(' '))
            else:
                row = []
                parts = line.strip('\n').split('    ')
                empty_part_count = 0
                for part in parts:
                    if part == '':
                        row.append(part)
                        empty_part_count += 1
                    else:
                        for val in part.split(' '):
                            # Removing brackets around crate name
                            crate_name = val[1:-1]
                            row.append(crate_name)
                            if crate_name == "":
                                empty_part_count += 1
                if empty_part_count != len(row):
                    stacks.append(row)
        
        # Transposing stacks
        stacks = [[val for val in row if val != ''] for row in zip(*stacks)]
        return stacks,operations


def find_top_crates(stacks,operations,reverse_crates=False):
    for op in operations:
        count,from_idx,to_idx = map(int,op[1::2])
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