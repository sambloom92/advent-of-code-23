from collections import Counter


def main():
    with open('input.txt', 'r') as input_file:
        ranked = sorted(
            [Hand(line.split(' ')[0], int(line.strip().split(' ')[1])) for line in input_file.readlines()],
        )
    for index, hand in enumerate(ranked):
        print(f"{(index + 1)} x {hand.bid} = {(index + 1) * hand.bid}")
    return sum([(index + 1) * hand.bid for index, hand in enumerate(ranked)])


class Card:
    def __init__(self, value: str):
        self.value = value
        self.rank = self.rank()

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.rank)

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def rank(self) -> int:
        try:
            return int(self.value)
        except ValueError:
            val_map = {
                'A': 14,
                'K': 13,
                'Q': 12,
                'J': 1,
                'T': 10,
            }
            return val_map[self.value]


class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand = [Card(card) for card in hand]
        self.bid = bid
        self.counter = Counter(self.hand)
        self.joker_count = self.counter.pop(Card('J'), 0)
        most_common_card = self.counter.most_common()[0][0] if self.joker_count != 5 else Card('J')
        self.counter.update([most_common_card]*self.joker_count)
        self.counts = sorted(list(self.counter.values()))
        self.rank = self.rank()

    def __lt__(self, other):
        if self.rank == other.rank:
            for this_card, that_card in zip(self.hand, other.hand):
                if this_card.rank == that_card.rank:
                    pass
                else:
                    return this_card.rank < that_card.rank
        else:
            return self.rank < other.rank

    def __eq__(self, other):
        return self.rank == other.rank and self.hand == other.hand

    def __repr__(self):
        return ','.join([str(card) for card in self.hand])

    def rank(self) -> int:
        if self.is_5_of_kind():
            return 7
        elif self.is_4_of_kind():
            return 6
        elif self.is_full_house():
            return 5
        elif self.is_3_of_kind():
            return 4
        elif self.is_2_pair():
            return 3
        elif self.is_2_of_kind():
            return 2
        elif self.is_high_card():
            return 1
        else:
            raise ValueError(f'hand could not be ranked: {self.hand}')

    def is_5_of_kind(self) -> bool:
        return self.counts == [5]

    def is_4_of_kind(self) -> bool:
        return self.counts == [1, 4]

    def is_3_of_kind(self) -> bool:
        return self.counts == [1, 1, 3]

    def is_2_of_kind(self) -> bool:
        return self.counts == [1, 1, 1, 2]

    def is_full_house(self) -> bool:
        return self.counts == [2, 3]

    def is_2_pair(self) -> bool:
        return self.counts == [1, 2, 2]

    def is_high_card(self) -> bool:
        return self.counts == [1, 1, 1, 1, 1]


if __name__ == '__main__':
    print(main())