import math


def main():
    with open('input.txt', 'r') as input_file:
        time_part, distance_part = input_file.readlines()
        time = int( time_part.split(":")[1].strip().replace(' ', ''))
        distance = int( distance_part.split(":")[1].strip().replace(' ', ''))
        sol_1, sol_2 = solve_quadratic(1, -time, distance * 1.000000001)
        print(f'{sol_1}, {sol_2}')
        return math.floor(sol_2) - math.floor(sol_1)


def solve_quadratic(a: int, b: int, c: float) -> tuple[float, float]:
    discriminant = math.sqrt(b**2 - 4 * a * c)
    return (-b - discriminant) / (2 * a), (-b + discriminant) / (2 * a)


if __name__ == '__main__':
    print(main())
