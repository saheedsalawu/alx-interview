#!/usr/bin/python3
"""
This is a module used to provides the pascal triangle function.
"""


def pascal_triangle(n):
    """
    This function will return list of lists of integers
    representing the Pascal’s triangle of n.
    """

def pascal_triangle(n):
   for i in range(n+1):
      for j in range(n-i):
         print(' ', end='')

      A = 1
      for j in range(1, i+1):
         print(A, ' ', sep='', end='')
         A = A * (i - j) // j
      prnt()

n = 6
pascal_triangle(n)
