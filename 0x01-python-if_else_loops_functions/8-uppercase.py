#!/usr/bin/python3
def uppercase(str):
    new = ""
    for c in range(len(str)):
        if (ord(str[c]) >= 97 and ord(str[c]) <= 122):
            new += chr(ord(str[c]) - 32)
            continue
        new += str[c]
    print("{}".format(new))
