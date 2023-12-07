# Part-1: 249748283
# Part-2: 248029057

from collections import Counter
from functools import cmp_to_key
import sys


class Card:
    hands_without_joker = "AKQJT98765432"
    joker_enabled = False

    def __init__(self, hands: str, value: int):
        self.hands = hands
        self.value = value
        self.normal_rank = self.get_rank_without_joker(hands)
        self.joker_rank = self.get_rank_with_joker(hands)

    @staticmethod
    def custom_comparator(card1: "Card", card2: "Card"):
        rank1, rank2 = card1.normal_rank, card2.normal_rank
        hands_order = Card.hands_without_joker
        if Card.joker_enabled:
            rank1, rank2 = card1.joker_rank, card2.joker_rank
            hands_order = "AKQT98765432J"
        if card1.hands == card2.hands:
            return 0
        if rank1 == rank2:
            for i, j in zip(card1.hands, card2.hands):
                if i != j:
                    return [1, -1][hands_order.index(i) > hands_order.index(j)]
        return [-1, 1][rank1 < rank2]

    @staticmethod
    def hands_comparator(a, b):
        return Card.custom_comparator(a, b)

    def get_rank_without_joker(self, hands):
        values = tuple(sorted(Counter(hands).values()))
        rank_dict = { (5,): 1, (1, 4): 2, (2, 3): 3, (1, 1, 3): 4, (1, 2, 2): 5,(1, 1, 1, 2): 6 }
        return rank_dict.get(values, 7)

    def get_rank_with_joker(self, hands):
        if "J" in hands:
            min_rank = 8
            for card in Card.hands_without_joker:
                if card != "J":
                    min_rank = min(min_rank, self.get_rank_without_joker(hands.replace("J", card)))
            return min_rank
        return self.get_rank_without_joker(hands)


def read_data(filename):
    cards = []
    with open(filename, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            hands, value = line.split(" ")
            value = int(value)
            cards.append(Card(hands, value))
    return cards


def day_7(cards: list[Card]):
    cards.sort(key=cmp_to_key(Card.hands_comparator))
    part_1_ans = sum(card.value * idx for idx, card in enumerate(cards, 1))

    Card.joker_enabled = True
    cards.sort(key=cmp_to_key(Card.hands_comparator))
    part_2_ans = sum(card.value * idx for idx, card in enumerate(cards, 1))
    return (part_1_ans, part_2_ans)


def main():
    filename = sys.argv[1]
    cards = read_data(filename)
    part_1_ans, part_2_ans = day_7(cards)
    print(f"Part-1: {part_1_ans}")
    print(f"Part-2: {part_2_ans}")


if __name__ == "__main__":
    main()
