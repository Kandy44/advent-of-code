import sys


def read_data(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return ''.join(line.strip("\n") for line in fp.readlines()).split(",")

def hash_algo(s):
    val = 0
    for ch in s:
        val = ((val + ord(ch)) * 17) % 256
    return val

def part_1(data):
    return sum(hash_algo(s) for s in data)

def part_2(data):
    boxes = [[] for _ in range(256)]
    focal_lengths = {}
    
    for s in data:
        if s[-1] == '-':
            key = s[:-1]
            idx = hash_algo(key)
            if key in boxes[idx]:
                boxes[idx].remove(key)
        else:
            key,value = s.split("=")
            value = int(value)
            idx = hash_algo(key)
            if key not in boxes[idx]:
                boxes[idx].append(key)
            focal_lengths[key] = value
            
    res = sum(box_num * lens_slot * focal_lengths[key] for box_num, box in enumerate(boxes, 1) for lens_slot, key in enumerate(box, 1) )
    return res

def main():
    filename = sys.argv[1]
    data = read_data(filename)
    part_1_ans, part_2_ans = part_1(data), part_2(data)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
