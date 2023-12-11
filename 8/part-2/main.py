from itertools import cycle
import math


def main():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    line_1 = lines[0].strip()
    map_lines = lines[2:]
    map = {
        line.split('=')[0].strip(): {
            'L': line.split('=')[1].split(',')[0].replace('(', '').strip(),
            'R': line.split('=')[1].split(',')[1].replace(')', '').strip(),
        }
        for line in map_lines
    }
    print(map)
    current_nodes = [key for key in map.keys() if key.endswith('A')]
    initial_steps = []
    for current_node in current_nodes:
        steps = 0
        directions = cycle(line_1)
        stop_loop = False
        while not stop_loop:
            current_direction = next(directions)
            steps += 1
            current_node = map[current_node][current_direction]
            stop_loop = current_node.endswith('Z')
        initial_steps.append(steps)
    return math.lcm(*initial_steps)


if __name__ == '__main__':
    print(main())
