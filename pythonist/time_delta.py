# from datetime import datetime, timedelta
import time
import datetime
class TimeDelta:
    def __init__(self):
        self.list = []
        self.T = 0
        self.month_mapping = {}
        self.month_mapping.update({"Jan": 1})
        self.month_mapping.update({"Feb": 2})
        self.month_mapping.update({"Mar": 3})
        self.month_mapping.update({"Apr": 4})
        self.month_mapping.update({"May": 5})
        self.month_mapping.update({"Jun": 6})
        self.month_mapping.update({"Jul": 7})
        self.month_mapping.update({"Aug": 8})
        self.month_mapping.update({"Sep": 9})
        self.month_mapping.update({"Oct": 10})
        self.month_mapping.update({"Nov": 11})
        self.month_mapping.update({"Dec": 12})


    def read_and_print_difference(self):
        self.N = int(raw_input())
        i = 0
        while i < self.N:
            # Sun 10 May 2015 13:54:36 -0700
            date1 = raw_input()
            t1 = time.mktime(datetime.datetime.strptime(date1, "%a %d %b %Y %H:%M:%S %z").timetuple())
            # t1= datetime.fromtimestamp(date1.split(" ")).strftime('%a %d %b %Y %H:%M:%S %z')
            date2 = raw_input()
            t2 = time.mktime(datetime.datetime.strptime(date2, "%a %d %b %Y %H:%M:%S %z").timetuple())
            print t2-t1
            # print t2
            i+=1


def main():
    delta = TimeDelta()
    delta.read_and_print_difference()

if __name__ == '__main__':
    main()




