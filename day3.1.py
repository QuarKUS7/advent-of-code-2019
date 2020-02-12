
with open('./input/day3', 'r') as f:
    input = f.read().splitlines()
wire1 = input[0].split(',')
wire2 = input[1].split(',')

from shapely.geometry import Point, LineString
from day3 import wire_path

ls1 = LineString(wire_path(wire1))
ls2 = LineString(wire_path(wire2))

cross = ls1.intersection(ls2)
cross_points = [c.coords[0] for c in cross]
cross_points.remove((0.0, 0.0))
print(cross_points)


def cut(line, distance):
    # Cuts a line in two at a distance from its starting point
    # This is taken from shapely manual
    if distance <= 0.0 or distance >= line.length:
        return [LineString(line)]
    coords = list(line.coords)
    for i, p in enumerate(coords):
        pd = line.project(Point(p))
        if pd == distance:
            return [
                LineString(coords[:i+1]),
                LineString(coords[i:])]
        if pd > distance:
            cp = line.interpolate(distance)
            return [
                LineString(coords[:i] + [(cp.x, cp.y)]),
                LineString([(cp.x, cp.y)] + coords[i:])]

