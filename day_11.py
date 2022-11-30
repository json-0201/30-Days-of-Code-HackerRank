#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

def hourglass(arr):
  """returns the maximum hourglass sum."""
  
  yes = [(0,0),(0,1),(0,2),(1,1),(2,0),(2,1),(2,2)]

  sum_final = 0
  for i,j in yes:
    sum_final += arr[i][j]
  
  for r in range(4):
    for c in range(4):
      sum_temp = 0
      
      for i,j in yes:
        sum_temp += arr[i+r][j+c]
  
      if sum_temp > sum_final:
        sum_final = sum_temp
    
  return sum_final

print(hourglass(arr))
