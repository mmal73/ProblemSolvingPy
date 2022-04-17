#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    max = n - 1
    aux = 0
    for i in range(n):
        for j in range(max):
            print(' ', end='')
        for k in range(i+1):
            print('#', end='')
        print('')
        max -= 1


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
