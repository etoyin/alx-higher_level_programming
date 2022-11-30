#!/usr/bin/python3
tracker = 1
for c in range(ord('z'), ord('a')+1, -1):
    if tracker % 2 == 0:
        print('{}'.format(chr(ord(c) - 32)), end='')
    else:
        print('{}'.format(chr(c)), end='')
    tracker = tracker + 1
