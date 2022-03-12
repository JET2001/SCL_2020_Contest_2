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

class Engineer:
    def __init__ (self, G_dist: int, A_dist: int):
        self.G_dist = G_dist
        self.A_dist = A_dist

    def has_wifi(self, range_G: int, range_A: int):
        if range_G >= self.G_dist and range_A >= self.A_dist: return False
        if range_G < self.G_dist and range_A < self.A_dist: return False
        return True


#### ========== MAIN IMPLEMENTATION ===========
## O(QE) time, where Q is the length of queries, and E is the length of engineers.
def question4(engineer_list: list, geofi_pt: Point, airfi_pt: Point, queries: list, n: int, q: int):
    ### Parse input
    geofi = BaseStation(geofi_pt.x, geofi_pt.y)
    airfi = BaseStation(airfi_pt.x, airfi_pt.y)
    engineers = []
    for e in engineer_list:
        g_dist = geofi.get_dist(e)
        a_dist = airfi.get_dist(e)
        engineers.append(Engineer(g_dist, a_dist))

    for query in queries:
        no_wifi_count = 0
        for e in engineers:
            if not e.has_wifi(query.G, query.A): no_wifi_count += 1
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
