from itertools import permutations

def intcode(inpt, signal, start):

    counter=0

    while True:
        instruction = f'{inpt[counter]:05}'
        o, modes = instruction[-2:], instruction[:-2]
        if o == '99':
            break
        if o == '01':
            a = inpt[inpt[counter+1]] if modes[-1] == '0' else inpt[counter+1]
            b = inpt[inpt[counter+2]] if modes[-2] == '0' else inpt[counter+2]
            c = inpt[counter+3]
            inpt[c] = a + b
            counter+= 4
        elif o == '02':
            a = inpt[inpt[counter+1]] if modes[-1] == '0' else inpt[counter+1]
            b = inpt[inpt[counter+2]] if modes[-2] == '0' else inpt[counter+2]
            c = inpt[counter+3]
            inpt[c] = a * b
            counter+= 4
        elif o == '03':
            a = inpt[counter+1]
            inpt[a] = signal
            signal = start
            counter+=2
        elif o == '04':
            a = inpt[counter+1]
            return inpt[a]
            counter+=2
        else:
            break


if  __name__== '__main__':
    with open('./input/day7', 'r') as f:
        input = f.read()
    input = eval(input)
    input = list(input)
    min_amp_out = 0
    import copy
    for i in permutations([0,1,2,3,4], 5):
        print(i)
        amp_out = 0
        for j in i:
            print(j)
            copy_input = copy.deepcopy(input)
            amp_out = intcode(copy_input, int(j), amp_out)
            print(amp_out)
        if not amp_out:
            continue
        if amp_out > min_amp_out:
            min_amp_out = amp_out
    print(min_amp_out)
    print(input)
