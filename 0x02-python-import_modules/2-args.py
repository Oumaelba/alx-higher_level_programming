#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("{}: {}".format(count, sys.argv[1]))
    else:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
