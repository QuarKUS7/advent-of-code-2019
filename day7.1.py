from itertools import permutations

class Amplifier:
    def __init__(self, signal, inpt):
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
            else:
                print(o)
                break


if  __name__== '__main__':
    with open('./input/day7', 'r') as f:
        input = f.read()
    input = eval(input)
    input = list(input)
    min_amp_out = 0
    max_out = 0
    import copy
    for i in permutations([5,6,7,8,9], 5):
        print(i)
        copy_input1 = copy.deepcopy(input)
        copy_input2 = copy.deepcopy(input)
        copy_input3 = copy.deepcopy(input)
        copy_input4 = copy.deepcopy(input)
        copy_input5 = copy.deepcopy(input)
        amp_out_prev=0
        amp0 = Amplifier(int(i[0]), copy_input1)
        amp1 = Amplifier(int(i[1]), copy_input2)
        amp2 = Amplifier(int(i[2]), copy_input3)
        amp3 = Amplifier(int(i[3]), copy_input4)
        amp4 = Amplifier(int(i[4]), copy_input5)
        programs = (amp0, amp1, amp2, amp3, amp4)
        while all(not program.halted for program in programs):
            for program in programs:
                amp_out = program.run_intcode(amp_out_prev)
                #import pdb; pdb.set_trace();
                if not program.halted:
                    amp_out_prev = amp_out
        if amp_out_prev > max_out:
            max_out = amp_out_prev
    print(max_out)

