#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if ord(i) >= 97 and ord(i) <= 123:
            i = chr(ord(i) - 32)
        print(f"{i}", end="")
    print("");
