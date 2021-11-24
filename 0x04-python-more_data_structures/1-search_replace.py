#!/usr/bin/python3
def search_replace(my_list, search, replace):
my_list = [search]
for abc, item in enumerate(my_list):
    if item == search:
        my_list[abc] = replace
print my_list
