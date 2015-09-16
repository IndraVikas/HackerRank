class StringFormat:
    def __init__(self):
        self.N = 0

    def read_data(self):
        self.N = int(raw_input())

    def print_different_format(self):
        i = 1
        length = len(str(bin(self.N))[2:])
        while i < self.N+1:
            dec = str(i)
            binary = str(bin(i))
            octal = str(oct(i))
            hexal = str(hex(i))
            # print "octal====", octal
            temp_str = dec.rjust(length)\
                       +" "+octal[1:].rjust(length)\
                       +" "+hexal[2:].rjust(length).upper()\
                       +" "+binary[2:].rjust(length)
            i += 1
            print temp_str


def main():
    string_format = StringFormat()
    string_format.read_data()
    string_format.print_different_format()

   # 17    21    11 10001
if __name__ == '__main__':
    main()


