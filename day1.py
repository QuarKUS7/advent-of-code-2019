import math


def compute_fuel(mass):
    return math.floor(mass / 3) - 2

if __name__ == '__main__':
    with open('./input/day1') as f:
        input = f.read().splitlines()
    output = sum([compute_fuel(int(module)) for module in input])
    print(output)
