#!/usr/bin/python3
for alpha in range(97, 123):
    if chr(alpha) not in 'eq':
        print("{}".format(chr(alpha)), end="")
