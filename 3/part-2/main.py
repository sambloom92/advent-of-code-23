import re
import math


def find_part_numbers(matrix: list[str]) -> list[int]:
    part_numbers = []
    for row_num, row in enumerate(matrix):
        gears = re.finditer(r'\*', row)
        for gear in gears:
            gear_index = gear.start()
            adjacent_nums = []
            if gear_index >= 0:
                if row_num:
                    row_above = matrix[row_num - 1]
                    adjacent_nums.extend(find_adjacent_numbers(gear_index, row_above))
                if row_num < len(matrix):
                    row_below = matrix[row_num + 1]
                    adjacent_nums.extend(find_adjacent_numbers(gear_index, row_below))
                adjacent_nums.extend(find_adjacent_numbers(gear_index, row))
            if len(adjacent_nums) == 2:
                part_numbers.append(math.prod(adjacent_nums))
    return part_numbers


def find_adjacent_numbers(gear_index, row):
    adjacent_nums = []
    above_matches = re.finditer(r'(\d+)', row)
    for match in above_matches:
        if gear_index - 1 <= match.start() <= gear_index + 1:
            adjacent_nums.append(int(match.group()))
        elif gear_index - 1 <= match.end() - 1 <= gear_index + 1:
            adjacent_nums.append(int(match.group()))
    return adjacent_nums


def main():
    with open('input.txt', 'r') as input_file:
        matrix = [line.strip() for line in input_file.readlines()]
        return sum(find_part_numbers(matrix))


if __name__ == '__main__':
    print(main())
