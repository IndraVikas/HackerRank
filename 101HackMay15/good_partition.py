class GoodPartition():
    def __init__(self):
        self.S = None

    def read_data(self):
        self.S = raw_input()

    def find_no_of_good_partition(self):
        l = []
        for i in range(0,26):
            l.append(0)
        for c in self.S:
            l[c-97] += 1
