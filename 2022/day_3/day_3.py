def read_data():
    return [l.strip() for l in open("../inputs/3.in", "r")]

def calculate_priorities(rucksacks,group_count=1,whole_rucksacks=False):
    priorities_sum = 0
    for i in range(0,len(rucksacks)-group_count+1,group_count):
        common_vals = set()
        if whole_rucksacks:
            common_vals = set(rucksacks[i]).intersection(*rucksacks[i+1:i+group_count])
        else:
            common_vals = set(rucksacks[i][:len(rucksacks[i])//2])
            common_vals = common_vals.intersection(rucksacks[i][len(rucksacks[i])//2:])
            for j in range(i+1,i+group_count):
                common_vals = common_vals.intersection(rucksacks[j][:len(rucksacks[j])//2])
                common_vals = common_vals.intersection(rucksacks[j][len(rucksacks[j])//2:])
        
        common_val = list(common_vals)[0]
        priorities_sum += ord(common_val)-(ord('a')-1 if common_val.islower() else ord('A')-27)

    return priorities_sum

def main():
    rucksacks = read_data()
    print(calculate_priorities(rucksacks,group_count=1,whole_rucksacks=False))
    print(calculate_priorities(rucksacks,group_count=3,whole_rucksacks=True))

main()