#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if i == j:
            continue
        elif j < i:
            continue
        elif i == 8 and j == 9:
            print("{}{}".format(i, j))
        print("{}{}".format(i, j), end=', ')
