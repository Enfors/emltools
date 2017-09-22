#!/usr/bin/env python3

"analyze.py -- data analytics tools."

import random

class Error(Exception):
    "Base class for exceptions in this module."

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "Error: %s" % self.msg

    def __repr__(self):
        return "Error(%s)" % self.msg


class BinScanError(Error):
    "Error raised by BinScan."
    pass


class BinScan():
    """
Search through a large dataset, looking for an error in a binary fashion.
"""

    def __init__(self, data):
        self.data = data

    def scan(self, start=0, end=None):
        "Scan the data, looking for the error."

        if end is None:
            print("END IS NONE!")
            end = len(self.data) - 1
            print("Fixed - end is now", end)

        data_len = end - start + 1
        middle_row = int(start + (data_len / 2))

        part_start = start
        part_end = middle_row - 1

        print("==== part 1")
        print("part_start:", part_start)
        print("part_end  :", part_end)
        
        if part_start <= part_end and self.check(part_start, part_end):
            self.scan(part_start, part_end)
            return True
        
        part_start = middle_row
        part_end = end
        
        print("==== part 2")
        print("part_start:", part_start)
        print("part_end  :", part_end)

        if part_start < part_end and self.check(part_start, part_end):
            self.scan(part_start, part_end)
            return True

        return False

    def check(self, start, end):
        print("Checking row %d through %d (%s)..." % (start, end,
                                                      self.data[start:end+1]))
        if self.check_for_error(self.data[start:end+1]):
            print("- Error found in range %d to %d." % (start + 1, end + 1))
            return True
        else:
            return False
        

    def check_for_error(self, data):
        if "Error" in data:
            return True
        else:
            return False
            


if __name__ == "__main__":
    data = []
    for item in range(0, 99):
        data.append(item)
    
    data[random.randint(20, 80)] = "Error"
    scanner = BinScan(data)
    scanner.scan()
