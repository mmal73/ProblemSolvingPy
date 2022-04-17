#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    s_len = len(s)
    am_pm_start = s_len - 2
    am_or_pm = s[am_pm_start:s_len]
    hours = s[0:2]
    int_hours = int(hours)
    new_hours = hours

    if am_or_pm == 'PM' and int_hours != 12:
        new_hours = str(int_hours + 12)
    elif am_or_pm == 'AM' and hours == '12':
        new_hours = '0' + str(int_hours - 12)

    s = s.replace(hours, new_hours)
    s = s.replace(am_or_pm, '')
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
