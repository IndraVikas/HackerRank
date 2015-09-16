import re

class RomanNumberValidator:
    def __init__(self):
        self.N = 0

    def read_data(self):
        self.N = raw_input()

    def is_valid_roman_number(self):
        match = re.search(r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', self.N)
        if match is not None:
            print "True"
        else:
            print "False"

def main():
    validator = RomanNumberValidator()
    validator.read_data()
    validator.is_valid_roman_number()

if __name__ == '__main__':
    main()