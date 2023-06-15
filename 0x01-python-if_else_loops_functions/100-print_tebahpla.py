#!/usr/bin/python3
i = 0
alphabet = ""

for c in range(ord('z'), ord('a') - 1, -1):
    alphabet += chr(c - i)
    i = 32 if i == 0 else 0

print("{}".format(alphabet), end="")
