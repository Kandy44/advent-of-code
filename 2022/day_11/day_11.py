from math import floor, prod
import copy


def read_monkeys():
    lines = []
    with open("../inputs/11.in", "r") as fp:
        lines = [line.strip('\n') for line in fp.readlines()]

    data = []
    for i in range(0, len(lines), 7):
        cur_monkey = Monkey(lines[i:i+7])
        data.append(cur_monkey)
    return data


class Monkey:
    def __init__(self, monkey_data: list[str]):
        self.monkey_id = int(monkey_data[0].split(' ')[-1][:-1])
        self.start_items = list(
            map(int, monkey_data[1].split(': ')[1].split(', ')))
        self.op = monkey_data[2].split('=')[1].strip().split(' ')[1:]
        self.test_val = int(monkey_data[3].split(' ')[-1])
        self.if_true = int(monkey_data[4].split(' ')[-1])
        self.if_false = int(monkey_data[5].split(' ')[-1])
        self.inspect_count = 0

    def add_items(self, items: int):
        self.start_items.extend(items)

    def update_items(self, mod_val, update_worry_level=True):
        op_char, val = self.op
        self.inspect_count += len(self.start_items)
        for idx in range(len(self.start_items)):
            cur_item = self.start_items[idx]
            cur_val = int(val) if val != 'old' else cur_item

            if op_char == '+':
                cur_val += cur_item
            if op_char == '-':
                cur_val -= cur_item
            if op_char == '*':
                cur_val *= cur_item
            if op_char == '/':
                cur_val //= cur_item

            if update_worry_level:
                cur_val = int(floor(cur_val/3))

            else:
                cur_val = cur_val % mod_val
            self.start_items[idx] = cur_val

    def print_items(self):
        print(self.start_items)


class MonkeyHandler:
    def __init__(self, monkeys: list[Monkey], update_worry_level=True):
        self.monkeys = monkeys
        self.update_worry_level = update_worry_level
        self.mod_val = prod([monkey.test_val for monkey in self.monkeys])

    def round(self):
        for cur_monkey in self.monkeys:
            cur_monkey.update_items(self.mod_val, self.update_worry_level)
            false_items = []
            true_items = [item for item in cur_monkey.start_items if item %
                          cur_monkey.test_val == 0 or false_items.append(item)]

            self.monkeys[cur_monkey.if_true].add_items(true_items)
            self.monkeys[cur_monkey.if_false].add_items(false_items)
            cur_monkey.start_items = []

    def get_monkey_business(self):
        inspect_count = sorted(
            [monkey.inspect_count for monkey in self.monkeys], reverse=True)
        return inspect_count[0]*inspect_count[1]

    def print_monkey_items(self):
        for monkey in self.monkeys:
            monkey.print_items()


def part_1(monkeys_list, round_count=20, update_worry_level=True):
    monkey_handler = MonkeyHandler(monkeys_list, update_worry_level)
    for _ in range(round_count):
        monkey_handler.round()

    monkey_business_level = monkey_handler.get_monkey_business()
    return monkey_business_level


def main():
    monkeys_list_1 = read_monkeys()
    monkeys_list_2 = copy.deepcopy(monkeys_list_1)
    print(part_1(monkeys_list_1, round_count=20, update_worry_level=True))
    print(part_1(monkeys_list_2, round_count=10000, update_worry_level=False))


main()
