#!/usr/bin/python3
def search_replace(my_list, search, replace):
   i = 0
   for j in my_list:
       if j == search:
           my_list.pop([i])
           my_list.insert(i, replace)
       i += 1
