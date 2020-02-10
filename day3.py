with open('./input/day3', 'r') as f:
    input = f.read().splitlines()
wire1 = input[0].split(',')
wire2 = input[1].split(',')
print(wire1)
print(wire2)

from shapely.geometry import LineString

def wire_path(wire):
    wire_path = [(0,0)]
    for i in wire:
        last_point = wire_path[-1]
        if i[0] == 'R':
            wire_path.append((last_point[0]+int(i[1:]),last_point[1]))
        if i[0] == 'L':
            wire_path.append((last_point[0]-int(i[1:]),last_point[1]))
        if i[0] == 'U':
            wire_path.append((last_point[0],last_point[1]+int(i[1:])))
        if i[0] == 'D':
            wire_path.append((last_point[0],last_point[1]-int(i[1:])))
    return wire_path

ls1 = LineString(wire_path(wire1))
ls2 = LineString(wire_path(wire2))

cross = ls1.intersection(ls2)
cross_points = [c.coords[0] for c in cross]
cross_points.remove((0.0, 0.0))
print(cross_points)

ds = [abs(t[0]) + abs(t[1])for t in cross_points]
print(ds)
print(min(ds))
