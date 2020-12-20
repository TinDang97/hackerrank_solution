#!/bin/python3
# link problem: https://www.hackerrank.com/challenges/non-divisible-subset/problem

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    frequency = [0] * k
    for num in s:
        frequency[num % k] += 1
    
    if k % 2 == 0:
        frequency[k//2] = min(frequency[k//2], 1)
        
    result = min(1, frequency[0])
    for i in range(1, k//2 + 1):
        result += max(frequency[i], frequency[k - i])
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
