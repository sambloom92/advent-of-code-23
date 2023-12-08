import re


def is_symbol(char: str) -> bool:
    return not (char.isdigit() or char == '.')


def find_part_numbers(matrix: list[str]) -> list[int]:
    part_numbers = []
    for row_num, row in enumerate(matrix):
        matches = re.finditer(r'(\d+)', row)
        for match in matches:
            adjacent_chars = ''
            start_col = max(match.start() - 1, 0)
            end_col = min(match.end(), len(row) - 1)
            adjacent_chars += row[start_col] if start_col else ''
            adjacent_chars += row[end_col] if end_col < len(row) else ''
            try:
                adjacent_chars += matrix[max(row_num - 1, 0)][start_col:end_col + 1]
                adjacent_chars += matrix[min(row_num + 1, len(matrix) - 1)][start_col:end_col + 1]
            except IndexError:
                pass
            if any(is_symbol(char) for char in adjacent_chars):
                part_numbers.append(int(match.group()))
    return part_numbers


def main():
    with open('input.txt', 'r') as input_file:
        matrix = [line.strip() for line in input_file.readlines()]
        return sum(find_part_numbers(matrix))


if __name__ == '__main__':
    print(main())
