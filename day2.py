
def intcode(input):

    counter=0

    while True:
        o,a,b,c = input[counter],input[counter+1],input[counter+2],input[counter+3]
        if o == 99:
            break
        if o == 1:
            input[c] = input[a] + input[b]
        elif o == 2:
            input[c] = input[a] * input[b]
        counter = counter + 4

    return input[0]

if  __name__== '__main__':
    with open('./input/day2', 'r') as f:
        input = f.read()

    input = eval(input)
    input = list(input)

    input[1]=12
    input[2]=2
    output = intcode(input)

    print(output)
