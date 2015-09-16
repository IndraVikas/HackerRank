class SortData:
    def __init__(self):
        self.list = []
        self.N = 0
        self.K = 0
        self.item_number_for_sorting = None

    def read_data(self):
        input1 = raw_input()
        # input2 = raw_input()
        self.N, self.K = [int(x) for x in input1.split()]
        i = 0
        while i < self.N:
            input2 = raw_input()
            l=[int(x) for x in input2.split()]
            i += 1
            self.list.append(l)
        self.item_number_for_sorting = int(raw_input())

    def get_item(self, item):
        return item[self.item_number_for_sorting]

    def sort_list(self):
        self.list.sort(key=self.get_item)
        # sorted(self.list, key=self.get_item)

    def print_data(self):
        i = 0
        while i < self.N:
          print(" ".join(str(x) for x in self.list[i]))
          i += 1


def main():
    sorting = SortData()
    sorting.read_data()
    sorting.sort_list()
    # print "item====", sorting.item_number_for_sorting
    sorting.print_data()

if __name__ == '__main__':
    main()




