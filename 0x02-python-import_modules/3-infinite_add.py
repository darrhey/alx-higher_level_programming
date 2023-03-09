#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count = len(argv)
    i = 1
    j = 0
    while i <= count:
        j += int(sys.argv[i])
        i += 1
    print("{}".format(j))
