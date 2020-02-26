
class Amplifier:
    def __init__(self, signal, inpt):
        self.relative_base = 0
        self.signal = signal
        self.first = True
        self.halted = False
        self.inpt = inpt
        self.counter = 0

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
                if self.first:
                    inpt[a] = self.signal
                    self.first = False
                else:
                    inpt[a] = start
                counter+=2
            elif o == '04':
                a = inpt[counter+1]
                counter+=2
                self.counter = counter
                print(inpt[a])
                return inpt[a]
            elif o == '05':
                a = inpt[inpt[counter+1]] if modes[-1] == '0' else inpt[counter+1]
                b = inpt[inpt[counter+2]] if modes[-2] == '0' else inpt[counter+2]
                if a != 0:
                    counter = b
                else:
                    counter+=3
            elif o == '06':
                a = inpt[inpt[counter+1]] if modes[-1] == '0' else inpt[counter+1]
                b = inpt[inpt[counter+2]] if modes[-2] == '0' else inpt[counter+2]
                if a == 0:
                    counter = b
                else:
                    counter+=3
            elif o == '07':
                a = inpt[inpt[counter+1]] if modes[-1] == '0' else inpt[counter+1]
                b = inpt[inpt[counter+2]] if modes[-2] == '0' else inpt[counter+2]
                c = inpt[counter+3]
                if a < b:
                    inpt[c] = 1
                else:
                    inpt[c] = 0
                counter+=4
            elif o == '08':
                a = inpt[inpt[counter+1]] if modes[-1] == '0' else inpt[counter+1]
                b = inpt[inpt[counter+2]] if modes[-2] == '0' else inpt[counter+2]
                c = inpt[counter+3]
                if a == b:
                    inpt[c] = 1
                else:
                    inpt[c] = 0
                counter+=4
            elif o == '09':
                a = inpt[counter+1]
                self.relative_base+= a
                print(a)
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
