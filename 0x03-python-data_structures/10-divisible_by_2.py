#!/usr/bin/python3
def divisible_by_2(my_list=[]):
   if not my_list:
      return None
   new = my_list.copy()
   for i in range(len(my_list)):
      if my_list[i] % 2 > 0:
         new[i] = False
      else:
         new[i] = True
   return new
