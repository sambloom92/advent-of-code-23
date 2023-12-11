from itertools import cycle
import re

def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    line_1 = lines[0].strip()
    map_lines = lines[2:]
    directions = cycle(line_1)
    map = {
        line.split('=')[0].strip(): {
            'L': line.split('=')[1].split(',')[0].replace('(', '').strip(),
            'R': line.split('=')[1].split(',')[1].replace(')\n', '').strip(),
        }
        for line in map_lines
    }
    print(map)
    steps = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        steps += 1
        current_node = map[current_node][next(directions)]
        print(steps)
        print(current_node)
    return steps




if __name__ == '__main__':
    print(main())
