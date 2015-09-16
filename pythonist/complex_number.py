
class ComplexNumber:
    def __init__(self):
        self.a1 = 0
        self.a2 = 0
        self.b1 = 0
        self.b2 = 0

    def read_data(self):
        self.a1, self.a2 = [int(x) for x in raw_input().split()]
        self.b1, self.b2 = [int(x) for x in raw_input().split()]

    def print_result_after_operation(self):
        c1 = complex(float(self.a1), float(self.a2))
        c2 = complex(float(self.b1), float(self.b2))
        self.print_complex_number(c1+c2)
        self.print_complex_number(c1-c2)
        self.print_complex_number(c1*c2)
        self.print_complex_number(c1/c2)
        # print c1+c2
        # print c1-c2
        # print c1*c2
        # print c1/c2
        print "%.2f" % pow(pow(self.a1,2)+pow(self.a2,2),0.5)
        print "%.2f" % pow(pow(self.b1,2)+pow(self.b2,2),0.5)

    def print_complex_number(self, c):
        c1 = float(c.real)
        c2 = float(c.imag)
        if c2 == 0.00:
            print "%.2f" % c1
            return
        if c1 == 0.00:
            print "%.2f" % c2+"i"
            return
        if c2 > 0.00:
            print "%.2f" % c1 +" + " + "%.2f" % c2+"i"
        else:
            print "%.2f" % c1 +" - " + "%.2f" % abs(c2)+"i"


def main():
    com_num = ComplexNumber()
    com_num.read_data()
    com_num.print_result_after_operation()

if __name__ == '__main__':
    main()