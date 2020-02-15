class IntCode:
    def __init__(self, input):
        self.input = input

    def process(self):
        counter=0

        while True:
            o,a,b,c = self.input[counter],self.input[counter+1],self.input[counter+2],self.input[counter+3]
            if o == 99:
                break
            if o == 1:
                self.input[c] = self.input[a] + self.input[b]
            elif o == 2:
                self.input[c] = self.input[a] * self.input[b]
            counter = counter + 4

        return self.input[0]

if  __name__== '__main__':
    with open('./input/day2', 'r') as f:
        input = f.read()

    input = eval(input)
    input = list(input)

    input[1]=12
    input[2]=2
    intcode = IntCode(input)
    output = intcode.process()

    print(output)
