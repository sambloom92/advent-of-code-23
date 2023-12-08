def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
        card_totals = {}
        for line in lines:
            card_num, num_matches = parse_card(line)
            card_totals[card_num] = {
                'matches': num_matches,
                'copies': 1,
            }
        for line_num, line in enumerate(lines):
            for num_copies in range(card_totals[line_num + 1]['copies']):
                for match in range(card_totals[line_num + 1]['matches']):
                    copy_card_num = line_num + match + 2
                    try:
                        card_totals[copy_card_num]['copies'] += 1
                    except KeyError:
                        pass
    return sum([val['copies'] for val in card_totals.values()])


def parse_card(line):
    card_num, card_info = line.split(':')
    card_num = int(card_num.split(' ')[-1])
    winning_part, have_part = card_info.split('|')
    winning_set = {int(num) for num in winning_part.strip().split(' ') if num}
    have_set = {int(num) for num in have_part.strip().split(' ') if num}
    num_matches = len(have_set.intersection(winning_set))
    return card_num, num_matches


if __name__ == '__main__':
    print(main())
