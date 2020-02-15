with open('input/day4', 'r') as f:
    input = f.read().splitlines()
pass_range = input[0].split('-')

class Password:
    def __init__(self, pass_range):
        self.start = int(pass_range[0])
        self.end = int(pass_range[1])

    def has_adjacent_digits(self, num):
        for i in range(5):
            if str(num)[i] == str(num)[i+1]:
                return True
        return False

    def is_non_decrease(self, num):
        digits = [int(d) for d in str(num)]
        for i in range(5):
            if not (digits[i] <= digits[i+1]):
                return False
        return True

    def compute_passwords(self):
        passwords = []
        for i in range(self.start,self.end+1):
            if self.has_adjacent_digits(i) and self.is_non_decrease(i):
                passwords.append(i)
        print(len(passwords))

p = Password(pass_range)
p.compute_passwords()
