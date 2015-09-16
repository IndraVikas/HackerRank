import re

class PhoneNumber:
    def __init__(self):
        self.list = []
        self.N = 0

    def read_data(self):
        self.N = int(raw_input())
        i = 0
        while i < self.N:
            self.list.append(raw_input())
            i+=1

    def is_phone_number(self):
        for item in self.list:
            match = re.search(r'((?:(?<!\d)\d{10}(?!\d)))', str(item))
            if match is not None:
                match = re.search(r'(^9\d+)|(^8\d+)|(^7\d+)', str(item))
                if match is not None:
                    print "YES"
                else:
                    print "NO"
            else:
                print "NO"


def main():
    phone_number = PhoneNumber()
    phone_number.read_data()
    phone_number.is_phone_number()

if __name__ == '__main__':
    main()




