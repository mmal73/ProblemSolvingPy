#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    new_grades = []
    attemps_to_sum = 3
    for grade in grades:
        if(grade >= 38):
            i = 1
            aux_grade = grade
            while(i < attemps_to_sum):
                aux_grade += 1
                if (aux_grade % 5 == 0):
                    grade = aux_grade
                    break
                i += 1
        new_grades.append(grade)

    return new_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
