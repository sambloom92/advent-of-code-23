DIGIT_WORDS = (
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
)


def find_spelled_digit(line: str, reverse_search: bool = False) -> int:
    line = line.lower()
    if reverse_search:
        line = line[::-1]
    for position, char in enumerate(line):
        if char.isdigit():
            return int(char)
        else:
            for digit, word in enumerate(DIGIT_WORDS):
                if reverse_search:
                    word = word[::-1]
                if line[position:].startswith(word):
                    return digit + 1


def line_digits(line: str) -> int:
    first = find_spelled_digit(line)
    last = find_spelled_digit(line, reverse_search=True)
    print(f"{first}{last}")
    return int(f"{first}{last}")


def main():
    with open('input.txt', 'r') as input_file:
        total = sum([line_digits(line) for line in input_file.readlines()])
    return total


if __name__ == '__main__':
    print(main())
