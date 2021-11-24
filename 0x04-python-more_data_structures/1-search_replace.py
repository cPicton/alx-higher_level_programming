#!/usr/bin/python3


def search_replace(my_list, search, replace):
    a_new_list = my_list[:]
    for x in range(len(a_new_list)):
        if a_new_list[x]  == search:
        a_new_list[x] = replace
    return a_new_list
