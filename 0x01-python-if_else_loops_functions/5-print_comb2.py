#!/usr/bin/python3
for i in range(100):
    if i < 10:
        i = '0'+i
    print("{}".format(i), end=', ')
    if i == 99:
        print("{}".format(i))
