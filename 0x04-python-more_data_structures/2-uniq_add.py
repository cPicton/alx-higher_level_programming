#!/usr/bin/python3
def uniq_add(my_list=[]):
    adds = 0
    x = set(my_list)
    for i in x:
        adds += i
    return adds
