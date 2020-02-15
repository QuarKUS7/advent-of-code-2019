
with open('./input/day3', 'r') as f:
    input = f.read().splitlines()
wire1 = input[0].split(',')
wire2 = input[1].split(',')

from day3 import Line, get_wire_lines, line_intersection

w = get_wire_lines(wire1)
w2 = get_wire_lines(wire2)

def point_on_line(line, point):
    if line.start[0] == line.end[0] == point[0] and line.start[1] <= point[1] <= line.end[1]:
        return abs(point[1] - line.start[1])
    if line.start[1] == line.end[1] == point[1] and line.start[0] <= point[0] <= line.end[0]:
        return abs(point[0] - line.start[0])

def compute_shortest_crossing(wire1, wire2):
    shortest = 999999
    x_len = 0
    y_len = 0
    for x in wire1:
        x_len = x_len + x.len
        y_len = 0
        for y in wire2:
            y_len = y_len + y.len
            h = line_intersection(x,y)
            if h and h != (0,0):
                ln1 = point_on_line(y, h)
                ln2 = point_on_line(x, h)
                cand = x_len + y_len - x.len - y.len + ln1 + ln2
                print(cand)
                if cand < shortest:
                    shortest = cand
    print(shortest)

w1 = get_wire_lines(wire1)
w2 = get_wire_lines(wire2)

compute_shortest_crossing(w1, w2)
