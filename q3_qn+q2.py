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
class Scenario:
    def __init__(self, type: str, node1 = None, node2 = None): ## one-index
        self.type = type
        self.node1 = node1 -1 if node1 != None else node1
        self.node2 = node2 -1 if node2 != None else node2



##### ========= UTILITY FUNCTIONS=======================
def BFSUtil(adj: list, visited: list, curr: int, num_visited: int):
    q = Queue()
    q.put(curr)
    while not q.empty():
        currNode = q.get()
        if visited[currNode] == True: continue ## visited before
        visited[currNode] = True
        num_visited += 1
        for neighbour in adj[currNode]: q.put(neighbour)
    return visited, num_visited ## updated visited list

def get_CCs(adj: list, n: int):
    ## O(N+Q) time | space
    num_visited = 0; curr = 0; num_cc = 0
    visited = [False] *n
    while (num_visited < n): # O(n) time
        if visited[curr] == True:
            curr += 1
            continue
        ## Only do DFS if it hasn't been visited before
        visited, num_visited = BFSUtil(adj, visited, curr, num_visited) ## BFS will be done on a subgraph
        ## Each time BFS is done, increment count by 1
        num_cc +=1

    return num_cc


#### ========== MAIN IMPLEMENTATION ===========
### O(Q(N+Q)) time | O(Q) space
def question3(scenario_list: list, q: int, n: int):
    ### Parse input
    adj = create_adjacency_list(n)
    push_order = Stack()
    for s in scenario_list: # O(Q)
        if s.type == "PUSH":
            push_order.put(s)
            adj[s.node1].append(s.node2)
            adj[s.node2].append(s.node1)
        else:
            most_recent_push = push_order.get()
            adj[most_recent_push.node1].pop() # O(1) - removing from the end of list
            adj[most_recent_push.node2].pop() # O(1) - removing from the end of list
            ## will be the most recent connection so the most recently added connection will be at the end of list.
        # O(N+Q)
        print(get_CCs(adj,n)) ## OUTPUT



### Read first line of input
var1, var2 = sys.stdin.readline().split()
q, n = int(var1), int(var2)
scenario_list = []
for i in range(q):
    ### INPUT HERE
    ##### First line of test case
    input  = sys.stdin.readline().split()
    if input[0] == 'PUSH':
        ## Create a push object
        push = Scenario("PUSH", int(input[1]), int(input[2]))
        scenario_list.append(push)
    else:
        pop = Scenario("POP")
        scenario_list.append(pop)
question3(scenario_list, q, n)
    # ### ANY OTHER INPUT SPECIFICS
    # ## =================================================
    #
    #
    # ## =================================================
    # ### PRINT OUTPUT
    # output = question3(scenario_list, ) ## EDIT PARAMS
    # print("Case {}: {}".format(i, output))
