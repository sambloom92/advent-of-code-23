import math

def main():
    with open('input.txt', 'r') as input_file:
        return sum([validate_line(line) for line in input_file.readlines()])


def validate_line(line):
    line = line.lower()
    game_id_part, game_info_part = line.split(':')
    min_nums = {
        'red': 0,
        'blue': 0,
        'green': 0,
    }
    for subset in game_info_part.split(';'):
        for color_sum in subset.split(','):
            color_num, color_name = color_sum.strip().split(' ')
            if int(color_num) > min_nums[color_name]:
                min_nums[color_name] = int(color_num)
    return math.prod(min_nums.values())


if __name__ == '__main__':
    print(main())
