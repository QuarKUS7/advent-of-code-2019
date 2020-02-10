import copy
from day2 import intcode

with open('./input/day2', 'r') as f:
    raw = f.read()

raw = eval(raw)
raw = list(raw)
for i in range(100):
    for j in range(100):
        input = copy.deepcopy(raw)
        input[1]=i
        input[2]=j
        if intcode(input) == 19690720:
            print((i,j))
            break
    else:
        continue
    break

