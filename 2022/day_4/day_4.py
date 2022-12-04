def read_data():
    with open("../inputs/4.in", "r") as fp:
        return [[ (lambda x1,x2: set(range(x1,x2+1)))(*map(int,j.split('-'))) for j in l.strip().split(',')] for l in fp]

def assignment_pair_count(ranges,check_overlap=False):
    if check_overlap:
        return sum(len(cur_range[0] & cur_range[1]) > 0 for cur_range in ranges)
    else:
        return sum(cur_range[0]<= cur_range[1] or cur_range[1] <= cur_range[0] for cur_range in ranges)

def main():
    ranges = read_data()
    print(assignment_pair_count(ranges,check_overlap=False))
    print(assignment_pair_count(ranges,check_overlap=True))

main()