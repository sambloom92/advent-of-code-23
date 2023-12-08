def line_digits(line: str) -> int:
    digits = [char for char in line if char.isdigit()]
    return int(f"{digits[0]}{digits[-1]}")


def main():
    with open('input.txt', 'r') as input_file:
        total = sum([line_digits(line) for line in input_file.readlines()])
    return total


if __name__ == '__main__':
    print(main())
