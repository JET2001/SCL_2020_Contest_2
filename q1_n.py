import math
import itertools
import collections
import sys
import bisect ## for bisection algorithms
import operator
import heapq
import functools
import decimal
import fractions
import random
import queue
import typing
### Declare any constants
POS_INF = float('inf')
NEG_INF = float('-inf')
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

### Declare any type aliases here
Queue = queue.Queue
Stack = queue.LifoQueue

#### UTILITY FUNCTIONS
### Creating a Matrix in Python
def create_matrix(rows, cols, default_val = 0):
    """
    Creates a matrix filled with default_val
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have

        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(default_val)

    return M
## =========== DEFINE ANY USER DEFINED CLASSES HERE ===============










#### ========== MAIN IMPLEMENTATION ===========
def question1(heights: list, L: int):
    '''OUTPUT A TUPLE of the height, index of maxpeak'''
    maxHeight, peak_idx = -1,-1
    for i in range(L):
        ## Go from left to right, treating every index as a ground.
        ## If it is not the ground, then move on.
        if heights[i] != 1: continue
        ## Otherwise, first consider the max height on the left
        currHeight, currPeak = 1, i
        while (currPeak > 0 and currHeight + 1 == heights[currPeak-1]):
            currPeak-=1
            currHeight+=1
        ## Breaks out of the while loop when we have found the peak or the start of the array.
        if currHeight > maxHeight:
            maxHeight = currHeight
            peak_idx = currPeak
        ## Now consider the maxc height on the right
        currHeight, currPeak = 1, i
        while (currPeak < L-1 and currHeight + 1 == heights[currPeak+1]):
            currPeak += 1
            currHeight += 1
        if currHeight > maxHeight:
            maxHeight = currHeight
            peak_idx = currPeak
    ### Parse input
    return (maxHeight, peak_idx)



### Read first line of input
num_test_cases = int(sys.stdin.readline()) ### template for input with test cases
for i in range(1,num_test_cases+1):
    ### INPUT HERE
    ##### First line of test case
    L = int(sys.stdin.readline())
    heights = sys.stdin.readline().split(); heights = [int(x) for x in heights]
    ### ANY OTHER INPUT SPECIFICS
    ## =================================================


    ## =================================================
    ### PRINT OUTPUT
    maxHeight, maxPeak = question1(heights, L) ## EDIT PARAMS
    print("Case #{}: {} {}".format(i, maxHeight, maxPeak))
