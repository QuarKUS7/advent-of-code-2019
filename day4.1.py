with open('input/day4', 'r') as f:
    input = f.read().splitlines()
pass_range = input[0].split('-')

from day4 import Password

class PasswordBetter(Password):
    def __init__(self, pass_range):
        super().__init__(pass_range)

    def has_adjecent_digits_no_group(self, num):
        if str(num)[0] == str(num)[1] != str(num)[2]:
            return True
        for i in range(1,4,1):
            if str(num)[i-1] != str(num)[i] == str(num)[i+1] != str(num)[i+2]:
                return True
        if str(num)[i-1] != str(num)[4] == str(num)[5] != str(num)[3]:
            return True

    def compute_better_password(self):
        passwords = []
        for i in range(self.start,self.end+1):
            if self.has_adjecent_digits_no_group(i) and self.is_non_decrease(i):
                passwords.append(i)
        print(len(passwords))
pb = PasswordBetter(pass_range)
pb.compute_better_password()
