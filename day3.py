with open('./input/day3', 'r') as f:
    input = f.read().splitlines()
wire1 = input[0].split(',')
wire2 = input[1].split(',')
print(wire1)
print(wire2)

class Line:
    def __init__(self, X, Y, Z):
        self.start = X
        self.end = Y
        self.len = Z

def get_wire_lines(wire):
    beg = (0, 0)
    wire_path = []
    wire_path.append(Line((0,0),(0,0),(0,0)))
    for i in wire:
        last_point = wire_path[-1]
        if i[0] == 'R':
            l = Line(last_point.end, (last_point.end[0]+int(i[1:]),last_point.end[1]), int(i[1:]))
            wire_path.append(l)
        if i[0] == 'L':
            l = Line(last_point.end, (last_point.end[0]-int(i[1:]),last_point.end[1]), int(i[1:]))
            wire_path.append(l)
        if i[0] == 'U':
            l = Line(last_point.end, (last_point.end[0], last_point.end[1]+int(i[1:])), int(i[1:]))
            wire_path.append(l)
        if i[0] == 'D':
            l = Line(last_point.end, (last_point.end[0], last_point.end[1]-int(i[1:])), int(i[1:]))
            wire_path.append(l)
    return wire_path

def line_intersection(line1, line2):
    xdiff = (line1.start[0] - line1.end[0], line2.start[0] - line2.end[0])
    ydiff = (line1.start[1] - line1.end[1], line2.start[1] - line2.end[1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0.0:
        return False

    d = (det(line1.start, line1.end), det(line2.start, line2.end))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (x, y)

def compute_crossing(wire1, wire2):
    for x in wire1:
        for y in wire2:
            h = line_intersection(x,y)
            if h:
                print(h)

w = get_wire_lines(wire1)
w2 = get_wire_lines(wire2)

compute_crossing(w, w2)

















#from shapely.geometry import LineString
#
#def wire_path(wire):
    #wire_path = [(0,0)]
    #for i in wire:
        #last_point = wire_path[-1]
        #if i[0] == 'R':
            #wire_path.append((last_point[0]+int(i[1:]),last_point[1]))
        #if i[0] == 'L':
            #wire_path.append((last_point[0]-int(i[1:]),last_point[1]))
        #if i[0] == 'U':
            #wire_path.append((last_point[0],last_point[1]+int(i[1:])))
        #if i[0] == 'D':
            #wire_path.append((last_point[0],last_point[1]-int(i[1:])))
    #return wire_path
#
#ls1 = LineString(wire_path(wire1))
#ls2 = LineString(wire_path(wire2))
#
#cross = ls1.intersection(ls2)
#cross_points = [c.coords[0] for c in cross]
#cross_points.remove((0.0, 0.0))
#print(cross_points)
#
#ds = [abs(t[0]) + abs(t[1])for t in cross_points]
#print(ds)
#print(min(ds))
