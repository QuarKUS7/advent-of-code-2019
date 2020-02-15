import copy
from day2 import IntCode

with open('./input/day2', 'r') as f:
    raw = f.read()

raw = eval(raw)
raw = list(raw)
for i in range(100):
    for j in range(100):
        input = copy.deepcopy(raw)
        input[1]=i
        input[2]=j
        intcode = IntCode(input)
        if intcode.process() == 19690720:
            print((i,j))
            break
    else:
        continue
    break

