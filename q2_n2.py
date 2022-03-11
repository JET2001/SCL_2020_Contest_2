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
def create_adjacency_list(num_of_nodes):
    """
    Initialises an adjacency list
    """
    adj_list = list()
    i = 0
    while (i < num_of_nodes):
        adj_list.append(list())
        i += 1
    return adj_list
## =========== DEFINE ANY USER DEFINED CLASSES HERE ===============








def updateLargest(maxPathSoFar: int, secondPath: int, newPath: int, max_start: int, max_end: int, second_start: int, second_end: int, new_start: int, new_end: int):
    ## Check that this path we're dealing with is unique, not the two paths here.
    if (new_start, new_end) == (second_start, second_end) or (new_start, new_end) == (second_end, second_start) or (new_start, new_end) == (max_start, max_end) or (new_start, new_end) == (max_end, max_start):
        return maxPathSoFar, secondPath, max_start, max_end, second_start, second_end
    if newPath <= secondPath:
        return maxPathSoFar, secondPath, max_start, max_end, second_start, second_end ## no change
    if newPath > secondPath and newPath <= maxPathSoFar:
        return maxPathSoFar, newPath, max_start, max_end,  new_start, new_end
    return newPath, maxPathSoFar, new_start, new_end, max_start, max_end

#### ========== MAIN IMPLEMENTATION ===========
def question2(adj: list, n: int): ## n is the number of nodes
    ### Parse input
    maxPathSoFar = INT_MIN + 1
    secondlongestPath = INT_MIN
    max_start, max_end, second_start, second_end = -1, -1, -1, -1
    # longest_path = dict()
    for i in range(n):
        visited = [False] * n
        curr_val = i
        path_list = queue.Queue()
        path_list.put((0, curr_val)) ## dist to node, node index.
        while not path_list.empty(): ## while path list is not empty
            curr_dist, curr_node = path_list.get()
            ## Check if the current distance is longer than the maxPath
            maxPathSoFar, secondlongestPath, max_start, max_end, second_start, second_end = updateLargest(maxPathSoFar, secondlongestPath, curr_dist, max_start, max_end,
            second_start, second_end, i, curr_node)

            ## mark this node as visited
            visited[curr_node] = True
            ## see outbound edges from this node
            for neighbour, dist in adj[curr_node]:
                if visited[neighbour] == True: continue ## backedge
                # if (curr_node, neighbour) in longest_path or (neighbour, curr_node) in longest_path:
                #     # dist_to_node = longest_path[(curr_node, neighbour)] if (curr_node, neighbour) in longest_path else longest_path[(neighbour, curr_node)
                ## Insert into queue
                path_list.put((curr_dist + dist, neighbour))
        # print("Node {} | Curr Dist: {} | MaxPathSoFar: {}".format(i+1, curr_dist, maxPathSoFar))
    return secondlongestPath
### Read first line of input
num_of_nodes = int(sys.stdin.readline()) ### template for input with test cases
adj_list = create_adjacency_list(num_of_nodes)
for i in range(1,num_of_nodes):
    ### INPUT HERE
    ##### First line of test case
    var1 , var2, var3  = sys.stdin.readline().split()
    src, dest, length = int(var1)-1, int(var2)-1, int(var3) ## decrement src vertex and destination vertex by 1 due to zero-indexed list
    adj_list[src].append((dest,length))
    adj_list[dest].append((src,length)) ## bidirectional graph
    ### PRINT OUTPUT
# print("Function call")
output = question2(adj_list, num_of_nodes) ## EDIT PARAMS
print(output)
