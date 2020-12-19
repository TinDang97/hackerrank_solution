#!/bin/python3

# link of problem: https://www.hackerrank.com/challenges/pairs/problem
# My solution using binary tree with O(N * log(N))
# if your array without duplicate elements, best solution is hash map
# Ref: https://www.geeksforgeeks.org/count-pairs-difference-equal-k/

import math
import os
import random
import re
import sys

class Tree():
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if self.value is None:
            self.value = value
            
        if value > self.value:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
    
    def find_node(self, value):
        if self.value is None:
            return None
        
        if self.value == value:
            return value
        
        if value > self.value:
            if self.right is None:
                return None
            return self.right.find_node(value)
        
        if self.left is None:
            return None
        return self.left.find_node(value)

def pairs(target, arr):
    num_paired = 0
    tree = Tree()
    for num in arr:
        for match_value in [num - target, num + target]:
            if match_value > 0 and tree.find_node(match_value):
                num_paired += 1
                print(match_value, num)
        tree.insert(num)
    return num_paired
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
