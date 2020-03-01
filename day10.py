from fractions import Fraction
import numpy


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_ratios(map, base, aster_count=0):
    asteroids_list = []
    hore = True
    dole = True
    vlavo = True
    vpravo = True
    for aster in map:
        if aster == base:
            continue
        if aster.x == base.x and aster.y > base.y:
            if dole:
                aster_count+=1
                dole = False
            continue
        if aster.x == base.x and aster.y < base.y:
            if hore:
                aster_count+=1
                hore = False
            continue
        if aster.y == base.y and aster.x < base.x:
            if vlavo:
                aster_count+=1
                vlavo = False
            continue
        if aster.y == base.y and aster.x > base.x:
            if vpravo:
                aster_count+=1
                vpravo = False
            continue
        asteroids_list.extend(numpy.arctan2(numpy.array([aster.x - base.x]),numpy.array([aster.y - base.y])))
    return aster_count, asteroids_list

def solution(asteroids):
    max_asters = 0
    for base in asteroids:
        acter_count, asteroids_list = get_ratios(asteroids, base)
        acter_count+= len(set(asteroids_list))
        if acter_count > max_asters:
            max_asters = acter_count
    print(max_asters)

def generate_map(input):
    aster_map = []
    for y, line in enumerate(input):
        for x, point in enumerate(line):
            if point == '#':
                aster_map.append(Asteroid(x, y))
    return aster_map

if __name__ == '__main__':
    with open('./input/day10', 'r') as f:
        input = f.read().splitlines()
    asteroids = generate_map(input)
    solution(asteroids)




