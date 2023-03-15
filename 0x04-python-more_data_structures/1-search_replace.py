#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    i = 0
        for j in new:
            if j == search:
                new.pop([i])
                new.insert(i, replace)
                i += 1
            else:
                i += 1
    return new
