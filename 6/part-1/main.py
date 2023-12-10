import math


def main():
    with open('input.txt', 'r') as input_file:
        time_part, distance_part = input_file.readlines()
        times = [int(num) for num in time_part.split(":")[1].strip().split(' ') if num]
        distances = [int(num) for num in distance_part.split(":")[1].strip().split(' ') if num]
        solutions = []
        for time, distance in zip(times, distances):
            sol_1, sol_2 = solve_quadratic(1, -time, distance * 1.000000001)
            solutions.append(math.floor(sol_2) - math.floor(sol_1))
    return math.prod(solutions)


def solve_quadratic(a: int, b: int, c: float) -> tuple[float, float]:
    discriminant = math.sqrt(b**2 - 4 * a * c)
    return (-b - discriminant) / (2 * a), (-b + discriminant) / (2 * a)


if __name__ == '__main__':
    print(main())
