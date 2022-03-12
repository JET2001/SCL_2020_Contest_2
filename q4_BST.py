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
class Point:
    def __init__ (self, x:int, y:int):
        self.x = x
        self.y = y

class Query:
    def __init__ (self, G: int, A: int):
        self.G = G
        self.A = A

class BaseStation:
    def __init__ (self, x: int, y: int):
        self.x = x
        self.y = y

    def get_dist(self, other: Point): ## O(1) time
        x, y = other.x, other.y
        return ((self.x - x)**2 + (self.y - y)**2)**0.5
    ## To see from the coordinates of an engineer whether it is in range of the base station
    # def within_range(self, other: Point): ## O(1) time
    #     return True if (self.get_dist(other) <= self.r) else False
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.num_desc = 0

    def is_leaf(self):
        return self.left == None and self.right == None

    def __lt__(self, other):
        return self.val < other.val

class BST:
    def __init__ (self):
        self.root = None

    def insert(self, val):
        newNode = BSTNode(val)
        ## if it is the first node in the BST
        if self.root == None:
            self.root = newNode
        else:
            currNode = self.root
            ## Find the node to insert
            while True:
                if newNode < currNode: ## __lt__ attribute has been overloaded
                    if currNode.has_left():
                        currNode = currNode.left
                        continue
                    else:
                        currNode.left = newNode
                        break
                else:
                    if currNode.has_right():
                        currNode = currNode.right
                        continue
                    else:
                        currNode.right = newNode
                        break
    def obtain_desc_util(self, currNode: BSTNode):
        num_descendants = 0
        if currNode.is_leaf():
            currNode.num_desc = 0
            return
        if currNode.has_left():
            obtain_desc_util(currNode.left)
            num_descendants += currNode.left.num_desc + 1
        if currNode.has_right():
            obtain_desc_util(currNode.right)
            num_descendants += currNode.right.num_desc + 1

    def obtain_descendants(self):
        self.obtain_desc_util(self.root)


#### ========== MAIN IMPLEMENTATION ===========
## O(QE) time, where Q is the length of queries, and E is the length of engineers.
def question4(engineers: list, geofi_pt: Point, airfi_pt: Point, queries: list, n: int, q: int):
    ### Parse input
    geofi = BaseStation(geofi_pt.x, geofi_pt.y, query.G)
    airfi = BaseStation(airfi_pt.x, airfi_pt.y, query.A)
    geofi_BST =
    for e in engineers:
        ## Compute distance f
    for query in queries:
        no_wifi_count = 0
        ## Instantiate both base stations
        geofi = BaseStation(geofi_pt.x, geofi_pt.y, query.G)
        airfi = BaseStation(airfi_pt.x, airfi_pt.y, query.A)
        #print(vars(geofi), vars(airfi))

        for e in engineers:
            if geofi.within_range(e) and airfi.within_range(e): no_wifi_count += 1
            elif geofi.within_range(e) == False and airfi.within_range(e) == False: no_wifi_count +=1
            else: pass
            #print(vars(e), no_wifi_count)
        print(no_wifi_count)





### Read first line of input
n = int(sys.stdin.readline()) ### template for input with test cases
engineers = list()
for i in range(n):
    ### INPUT HERE
    ##### First line of test case
    var1 , var2  = sys.stdin.readline().split()
    x, y = int(var1), int(var2)
    engineers.append(Point(x,y))
stn = sys.stdin.readline().split()
geofi = Point(int(stn[0]), int(stn[1]))
airfi = Point(int(stn[2]), int(stn[3]))
q = int(sys.stdin.readline())
queries = list()
for i in range(q):
    var1, var2 = sys.stdin.readline().split()
    rg, ra = int(var1), int(var2)
    queries.append(Query(rg, ra))

    ### PRINT OUTPUT
question4(engineers, geofi, airfi, queries, n, q) ## EDIT PARAMS
