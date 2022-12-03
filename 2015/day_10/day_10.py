from itertools import groupby
def read_data():
    with open("../inputs/10.in", "r") as fp:
        return fp.readline().strip()

def update_sequence(s):
    return "".join([str(len(list(group)))+str(num) for (num,group) in groupby(list(s))])

def look_and_say(inp,n):
    res = inp
    for _ in range(n):
        res = update_sequence(res)
    return res

def main():
    inp = read_data()
    part_1_ans = look_and_say(inp,n=40)
    part_2_ans = look_and_say(part_1_ans,n=10)
    print(len(part_1_ans))
    print(len(part_2_ans))

main()