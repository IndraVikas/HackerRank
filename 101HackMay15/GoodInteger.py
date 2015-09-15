__author__ = 'iv'


class GoodInteger:
    def __init__(self):
        self.n = None
        self.L = None
        self.R = None
        self.A = []
        self.output = []

    def read_data(self):
        input1 = raw_input()
        input2 = raw_input()
        self.n, self.L, self.R = [int(x) for x in input1.split()]
        self.A = [int(x) for x in input2.split()]

    def is_between_L_R(self, i):
        if(i>=self.L and i <= self.R):
            return True
        return False;

    def is_between_L_1_R_1(self, i):
        if(i>=self.L-1 and i <= self.R+1):
            return True
        return False;

    def find_number_of_operations(self, i):
        count  = 0
        if (i < self.L):
            count = self.L - i
        if i > self.R:
            count =  i - self.R
        return count

    def find_change_count(self):
        count = []
        for i in self.A:
            if not self.is_between_L_R(i):
                count.append(self.find_number_of_operations(i))
            else:
                count.append(0)
        # sorted(count)
        count.sort()
        sum = 0
        sum_list = []
        for i in range(self.n):
            sum = sum + count[i]
            sum_list.append(sum)
        # print "count", count
        # sorted(sum_list,reverse=True)
        # print "sum=", sum_list
        for i in range(1, self.n+1):
            print sum_list[self.n - i],
        print


def main():
    T = int(raw_input())
    i = 0;
    good_integer = GoodInteger()
    while i < T:
        good_integer.read_data()
        good_integer.find_change_count()
        i += 1

if __name__ == '__main__':
    main()