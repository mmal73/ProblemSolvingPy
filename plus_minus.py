#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    total = len(arr)
    positive_nums, negative_nums, zero_nums = 0, 0, 0
    for num in arr:
        if(num > 0):
            positive_nums += 1
        elif(num < 0):
            negative_nums += 1
        else:
            zero_nums += 1
    print("%.6f" % (positive_nums/total))
    print("%.6f" % (negative_nums/total))
    print("%.6f" % (zero_nums/total))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
