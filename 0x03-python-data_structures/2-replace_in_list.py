#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
   if idx < 0:
       return my_list
       continue
   elif idx >= len(my_list):
       return my_list
       continue
   else:
       my_list[idx] = element
       return my_list
