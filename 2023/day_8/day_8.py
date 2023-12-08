# Part-1: 17621
# Part-2: 20685524831999

import math
import re
import sys


def read_data(filename):
    select_order = []
    travel_map = {}
    with open(filename, "r", encoding="utf-8") as fp:
        select_order = [{"L": 0, "R": 1}[ch] for ch in fp.readline().strip("\n")]
        _ = fp.readline()
        travel_map = { cur_place: [left_way, right_way] for cur_place, left_way, right_way in 
		       map(lambda line: re.search(r"(\w+) = \((\w+), (\w+)\)", line).groups(), fp.readlines()) 
		     }
    return select_order, travel_map


def step_count(select_order, travel_map, start_node, end_node):
    count = 1
    cur_idx = 0
    order_len = len(select_order)
    travel_idx = select_order[cur_idx % order_len]
    while not travel_map[start_node][travel_idx].endswith(end_node):
        start_node = travel_map[start_node][travel_idx]
        cur_idx += 1
        travel_idx = select_order[cur_idx % order_len]
        count += 1
    return count


def day_8(select_order, travel_map, nodes_lst):
    part_1_ans, part_2_ans = [
        math.lcm(*[step_count(select_order, travel_map, start_node, end_node) for start_node in start_nodes])
        for start_nodes, end_node in nodes_lst
    ]
    return part_1_ans, part_2_ans


def main():
    filename = sys.argv[1]
    select_order, travel_map = read_data(filename)
    start_nodes = [node for node in travel_map if node.endswith("A")]
    nodes_lst = [[["AAA"], "ZZZ"], [start_nodes, "Z"]]
    part_1_ans, part_2_ans = day_8(select_order, travel_map, nodes_lst)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
