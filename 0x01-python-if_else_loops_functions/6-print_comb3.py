#!/usr/bin/python3
list = []
for i in range(90):
    if i % 11 == 0:
        continue
    elif (i%10)*10)+(i/10) in list:
        continue
    list.append(i)
for j in list:
    if j == 89:
        print("{:02d}".format(j))
    else:
        print("{:02d}".format(j), end=', ')
