#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    output_valid = "YES"
    repetitions = {}
    for i in range(len(s)):
        letter = s[i]
        if letter in repetitions:
            repetitions[letter] += 1
        else:
            repetitions[letter] = 1

    letters_with_other_number_of_repetitions = 0
    first_key = list(repetitions.keys())[0]
    reference_item = repetitions.pop(first_key)

    while len(repetitions) > 0:
        item = repetitions.pop(list(repetitions.keys())[0])
        if reference_item != item:
            letters_with_other_number_of_repetitions += 1

    if letters_with_other_number_of_repetitions > 1:
        output_valid = "NO"

    return output_valid


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
