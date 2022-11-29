#!/bin/python3

import math
import os
import random
import re
import sys
 
if __name__ == '__main__':
    n = int(input().strip())

    
binary = []

while int(n/2) != 0:
  binary.append(n%2)
  n=int(n/2)
binary.append(1)

if n==0:
  binary = [0]

binary.reverse()
binary="".join(list(map(str,binary)))

consecutive=[num[0] for num in re.findall(r'(([1])\2+)', binary)]

if not consecutive:
  print(1)
else:
  print(len(max(consecutive)))
