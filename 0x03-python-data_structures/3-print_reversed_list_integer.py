#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    limit = my_list[::-1]
    for i in limit:
        print("{:d}".format(limit[i]))
