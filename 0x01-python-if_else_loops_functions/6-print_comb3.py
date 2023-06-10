#!/usr/bin/python3
for num in range(89):
    if num / 10 < num % 10:
        print("{:02}, ".format(num), end="")
print("89")
