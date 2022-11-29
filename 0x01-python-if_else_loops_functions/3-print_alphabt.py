#!/usr/bin/python3
for c in range(ord('a'), ord('z')+1):
    if c is ord('e') or c is ord('q'):
        continue
    print('{}'.format(chr(c)), end='')
