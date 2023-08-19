#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    arg_count = len(sys.argv) - 1
    for i in range(1, len(sys.argv)):
        num = int(sys.argv[i])
        sum += num
    print("{}".format(sum))
