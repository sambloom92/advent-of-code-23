def main():
    with open('input.txt', 'r') as input_file:
        return sum([card_total(line) for line in input_file.readlines()])


def card_total(line: str) -> int:
    winning_part, have_part = line.split(':')[-1].split('|')
    winning_set = {int(num) for num in winning_part.strip().split(' ') if num}
    have_set = {int(num) for num in have_part.strip().split(' ') if num}
    matches = have_set.intersection(winning_set)
    return 2 ** (len(matches) - 1) if matches else 0


if __name__ == '__main__':
    print(main())
