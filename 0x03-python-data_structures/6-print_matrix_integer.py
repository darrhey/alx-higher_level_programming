#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
   for i in range(len(matrix)):
      len = len(matrix[i])
      for j in range(len):
         if j != len - 1:
            endchar = ' '
         else:
            endchar = ''
         print("{:d}".format(matrix[i][j]), end=endchar)
      print("")
