TOTALS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def main():
    with open('input.txt', 'r') as input_file:
        return sum([validate_line(line) for line in input_file.readlines()])


def validate_line(line):
    line = line.lower()
    game_id_part, game_info_part = line.split(':')
    game_id = int(game_id_part.split(' ')[-1])
    for subset in game_info_part.split(';'):
        for color_sum in subset.split(','):
            color_num, color_name = color_sum.strip().split(' ')
            if TOTALS[color_name] < int(color_num):
                print(line)
                return 0
    return game_id


if __name__ == '__main__':
    print(main())
