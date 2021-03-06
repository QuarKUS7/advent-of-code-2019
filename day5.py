def intcode(input):

    counter=0

    while True:
        instruction = f'{input[counter]:05}'
        o, modes = instruction[-2:], instruction[:-2]
        if o == '99':
            break
        if o == '01':
            a = input[input[counter+1]] if modes[-1] == '0' else input[counter+1]
            b = input[input[counter+2]] if modes[-2] == '0' else input[counter+2]
            c = input[counter+3]
            input[c] = a + b
            counter+= 4
        elif o == '02':
            a = input[input[counter+1]] if modes[-1] == '0' else input[counter+1]
            b = input[input[counter+2]] if modes[-2] == '0' else input[counter+2]
            c = input[counter+3]
            input[c] = a * b
            counter+= 4
        elif o == '03':
            a = input[counter+1]
            input[a] = 1
            counter+=2
        elif o == '04':
            a = input[counter+1]
            print(input[a])
            counter+=2
        else:
            print("Unknown o")

    return input[0]

if  __name__== '__main__':
    with open('./input/day5', 'r') as f:
        input = f.read()

    input = eval(input)
    input = list(input)
    print(input)
    output = intcode(input)

