import math
from day1 import compute_fuel



def compute_full_fuel(mass):
    fuel = compute_fuel(mass) 
    if fuel <= 0:
        return 0
    else:
        return fuel + compute_full_fuel(fuel)

if __name__== '__main__':
    with open('./input/day1', 'r') as f:
        input = f.read().splitlines()
    output = sum([compute_full_fuel(int(mod)) for mod in input])
    print(output)
