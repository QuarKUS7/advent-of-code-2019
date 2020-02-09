
if __name__== '__main__':
    with open('./input/day2', 'r') as f:
        input = f.read()
    print(type(input))
    input = eval(input)
    input = list(input)
    print(input)
    input[1]=12
    input[2]=2
    counter=0
    while True:
        o,a,b,c = input[counter],input[counter+1],input[counter+2],input[counter+3]
        if 99 in [o,a,b,c]:
            break
        if o==1:
            input[c] = input[a] + input[b]
        elif o==2:
            input[c]=input[a]*input[b]
        counter = counter + 1
        print(counter)
    print(input[0])
