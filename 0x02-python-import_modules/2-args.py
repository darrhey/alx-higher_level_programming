#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count = len(argv)
    i = 1
    if count == 0:
        print("{} argument.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(i, sys.argv[1]))
    else:
        print("{} arguments:".format(count))
        while i <= count:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
