#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

for i in range(1,int(n/2)+1):
    temp = arr[i-1]
    arr[i-1] = arr[n-i]
    arr[n-i] = temp
      
for i in range(n):
    print(arr[i], end=" ")
