#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        values = []
        for x in my_list:
            if x % 2 is 0:
                values.append(True)
            else:
                values.append(False)
        return values
