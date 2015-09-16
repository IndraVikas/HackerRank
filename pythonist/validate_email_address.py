import re

class EmailAddressValidator:
    def __init__(self):
        self.list = []
        self.N = 0
        self.output = []

    def read_data(self):
        self.N = int(raw_input())
        i = 0
        while i < self.N:
            self.list.append(raw_input())
            i+=1

    def is_valid_email_address(self):

        for item in self.list:
            # print item
            match = re.search(r'\b[A-Za-z0-9_-]{1,}@[A-Za-z0-9]{1,}\.\w{1,3}\b', str(item))
            if match is not None:
                self.output.append(item)

    # ([A-Z|a-z|0-9|_|-])@([A-Za-z0-9])\.([A-Za-z]{3})\b
    def print_email_address(self):
        print sorted(self.output)


def main():
    validator = EmailAddressValidator()
    validator.read_data()
    validator.is_valid_email_address()
    validator.print_email_address()

if __name__ == '__main__':
    main()




