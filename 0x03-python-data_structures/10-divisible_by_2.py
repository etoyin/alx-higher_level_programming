#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newL = []
    for i in my_list:
        if i % 2 == 0:
            newL.append(True)
        else:
            newL.append(False)
    return newL
