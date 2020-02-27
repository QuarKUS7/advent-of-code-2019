
class Amplifier:
    def __init__(self, signal, inpt):
        self.relative_base = 0
        self.signal = signal
        self.first = True
        self.halted = False
        self.inpt = inpt
        self.counter = 0

    def find_value(self, mode, param):
        if mode == '0':
            return self.inpt[param]
        elif mode == '1':
            return param
        elif mode == '2':
            return self.inpt[self.relative_base + param]

    def run_intcode(self, start):
        inpt = self.inpt
        counter =  self.counter
        while True:
            instruction = '{0:05d}'.format(inpt[counter])
            o, modes = instruction[-2:], instruction[:-2]
            if o == '99':
                self.halted = True
                break
            if o == '01':
                a = self.find_value(modes[-1], inpt[counter+1])
                b = self.find_value(modes[-2], inpt[counter+2])
                c = self.relative_base + inpt[counter+3] if modes[-3] == '2' else inpt[counter+3]
                inpt[c] = a + b

                counter+= 4
            elif o == '02':
                a = self.find_value(modes[-1], inpt[counter+1])
                b = self.find_value(modes[-2], inpt[counter+2])
                c = self.relative_base + inpt[counter+3] if modes[-3] == '2' else inpt[counter+3]
                inpt[c] = a * b
                counter+= 4
            elif o == '03':
                a = self.relative_base + inpt[counter+1] if modes[-1] == '2' else inpt[counter+1]
                #a = inpt[counter+1]
                inpt[a] = start
                counter+=2
            elif o == '04':
                a = self.find_value(modes[-1], inpt[counter+1])
                counter+=2
                print(a)
            elif o == '05':
                a = self.find_value(modes[-1], inpt[counter+1])
                b = self.find_value(modes[-2], inpt[counter+2])
                if a != 0:
                    counter = b
                else:
                    counter+=3
            elif o == '06':
                a = self.find_value(modes[-1], inpt[counter+1])
                b = self.find_value(modes[-2], inpt[counter+2])
                if a == 0:
                    counter = b
                else:
                    counter+=3
            elif o == '07':
                a = self.find_value(modes[-1], inpt[counter+1])
                b = self.find_value(modes[-2], inpt[counter+2])
                c = self.relative_base + inpt[counter+3] if modes[-3] == '2' else inpt[counter+3]
                if a < b:
                    inpt[c] = 1
                else:
                    inpt[c] = 0
                counter+=4
            elif o == '08':
                a = self.find_value(modes[-1], inpt[counter+1])
                b = self.find_value(modes[-2], inpt[counter+2])
                c = self.relative_base + inpt[counter+3] if modes[-3] == '2' else inpt[counter+3]
                if a == b:
                    inpt[c] = 1
                else:
                    inpt[c] = 0
                counter+=4
            elif o == '09':
                a = self.find_value(modes[-1], inpt[counter+1])
                #a = inpt[counter+1]
                self.relative_base+= a
                counter+=2
            else:
                print(o)
                break

if  __name__== '__main__':
    with open('./input/day9', 'r') as f:
        input = f.read()
    input = eval(input)
    input = list(input) + [0] * 100
    min_amp_out = 0
    max_out = 0
    amp0 = Amplifier(1, input)
    amp0.run_intcode(1)
