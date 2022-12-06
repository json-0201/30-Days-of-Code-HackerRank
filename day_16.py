#!/bin/python3

import math
import os
import random
import re
import sys

S = input()

try:
    S = int(S)
    print(S)
except Exception as e:
    print("Bad String")
