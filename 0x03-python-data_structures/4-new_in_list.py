#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = my_list[:]
    if 0 <= idx < len(newList):
        newList[idx] = element
    return newList
