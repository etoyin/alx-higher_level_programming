#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = -1
    limit = -1 * len(my_list)
    while i >= limit:
        print("{:d}".format(my_list[i]))
        i = i - 1
