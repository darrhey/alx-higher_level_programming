#!/usr/bin/python3

def no_c(my_string):
   new_string = ""
   if my_string or len(my_string) > 0:
       for i in my_string:
           if i is not 'C' and i is not 'c':
               new_string += i
               my_string = new_string
   return my_string
