import ast
from math import prod,ceil
import functools

def read_data() -> list[list]:
    lines = []
    with open("../inputs/13.in", "r") as fp:
        for line in fp:
            cur_s = line.strip('\n')
            if len(cur_s) > 0:
                cur_list = ast.literal_eval(line.strip('\n'))
                lines.append(cur_list)
    return lines
    
def compare_lists(l1:list,l2:list) -> int:
    if isinstance(l1,int) and isinstance(l2,int):
        if l1 < l2:
            return -1
        elif l1 > l2:
            return 1
        return 0
    
    elif isinstance(l1,list) and isinstance(l2,list):
        i1 = 0
        n1,n2=len(l1),len(l2)
        while i1 < n1 and i1 < n2:
            comp_val = compare_lists(l1[i1],l2[i1])
            if comp_val != 0:
                return comp_val
            i1 += 1
        return -1 if n1 < n2 else 1 if n1 > n2 else 0
    else:
        if isinstance(l1,int):
            l1 = [l1]
        elif isinstance(l2,int):
            l2 = [l2]
        return compare_lists(l1,l2)


def pair_idxs_sum(packets: list[list],divider_packets: list[int]) -> int:
    count = 0
    decoder_key = 1
    i = 0
    n = len(packets)
    
    while i < n:
        l1,l2 = packets[i],packets[i+1]
        if compare_lists(l1,l2) == -1:
            count += (ceil(i/2) + 1)
        i += 2
    
    packets.extend(divider_packets)
    packets.sort(key=functools.cmp_to_key(compare_lists))
    decoder_key = prod(packets.index(div_packet)+1 for div_packet in divider_packets)
    return (count,decoder_key)

def main():
    data = read_data()
    divider_packets=[[[2]],[[6]]]
    day_12_ans = pair_idxs_sum(data,divider_packets=divider_packets)
    print('\n'.join(map(str,day_12_ans)))

main()