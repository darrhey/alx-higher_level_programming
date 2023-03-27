#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listed = 0
    for y in range(0, x):
        try:
            print('{}'.format(my_list[y]), end='')
            listed += 1
        except:
            continue
    print()
    return listed
