#!/usr/bin/python3
def no_c(my_string):
    lenght = len(my_string)
    i = 0
    new_s = my_string[:]
    for char in range(lenght):
        if (my_string[char] == 'c' or my_string[char] == 'C'):
            new_s = new_s[:(char - i)] + my_string[(char + 1):]
            i += 1
    return new_s
