from __future__ import annotations


def main():
    with open('input.txt', 'r') as input_file:
        base_sequences = [[int(num) for num in line.strip().split(' ')] for line in input_file.readlines()]
    vals = [SensorSequence(seq).previous_value for seq in base_sequences]
    return sum(vals)


class SensorSequence:
    def __init__(self, base_sequence: list[int]):
        self.base_sequence = base_sequence
        self.iterator = iter(self.base_sequence)
        self.next_order_sequence: SensorSequence | None = self.get_next_order_sequence()

    def get_next_order_sequence(self) -> SensorSequence | None:
        if all([num == 0 for num in self.base_sequence]):
            return None
        sequence_values = [
            next_num - num
            for num, next_num in zip(
                self.base_sequence[:-1],
                self.base_sequence[1:],
            )
        ]
        return SensorSequence(sequence_values)

    @property
    def first_value(self) -> int:
        return self.base_sequence[0]

    @property
    def previous_value(self) -> int:
        if self.next_order_sequence:
            return self.first_value - self.next_order_sequence.previous_value
        else:
            return 0


if __name__ == '__main__':
    print(main())
