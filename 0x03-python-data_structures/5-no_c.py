#!/usr/bin/python3

def no_c(my_string):
   while my_string.find("c") != -1:
      my_string.pop(my_string.find("c"))
   while my_string.find("C") != -1:
      my_string.pop(my_string.find("C"))
   return my_list
