#!/bin/python3
# problem link: https://www.hackerrank.com/challenges/sherlock-and-array/problem


import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    left_sum = 0
    right_sum = sum(arr)
    for elm in arr: 
        if abs((right_sum - elm) - left_sum) < 0.001:
            return "YES"
        left_sum += elm
        right_sum -= elm
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
