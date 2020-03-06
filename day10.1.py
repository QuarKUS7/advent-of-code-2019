
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
            elif point == 'X':
                base = Asteroid(x,y)
    return aster_map, base
import math

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

print(getAngle((5, 0), (0, 0), (0, 5)))
if __name__ == '__main__':
    with open('./input/day10', 'r') as f:
        input = f.read().splitlines()
    asteroids, base = generate_map(input)
    #solution(asteroids)
    first = [aster for aster in asteroids if aster.x == base.x and aster.y < base.y]
    first_met = first[0]
    for a in first:
        if base.y - a.y < base.y - first_met.y:
            first_met = a
    asteroids.remove(first_met)

    print("First:", first_met.x, first_met.y)
    print(len(first))
    next_aster = None
    old_angle = 0.1
    count = 1
    while asteroids != []:
        min_angle = 3000
        for i in asteroids:
            angle = getAngle((first_met.x, first_met.y), (base.x,base.y), (i.x,i.y))
            if angle <= old_angle:
                continue
            if angle < min_angle:
                min_angle = angle
                next_aster = i
            elif angle == min_angle:
                print("ano")
                if base.y - i.y < base.y - next_aster.y:
                    next_aster = i
        if min_angle == 3000:
            first = [aster for aster in asteroids if aster.x == base.x and aster.y < base.y]
            import pdb; pdb.set_trace();

            first_met = first[-1]
            for a in first:
                if base.y - a.y < base.y - first_met.y:
                    first_met = a
            #asteroids.remove(first_met)
            next_aster = first_met
            min_angle = 0
        count +=1
        print("position:", next_aster.x, next_aster.y)
        print("min angle:", min_angle)
        print("count:", count)
        asteroids.remove(next_aster)
        #import pdb; pdb.set_trace();
        if count == 200:
            break
        old_angle = min_angle


