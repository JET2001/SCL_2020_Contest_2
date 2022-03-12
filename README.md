# SCL_2020_Contest_2
---
### Q1: Highest Mountain
O(n) time | O(1) space
Traverse the array from left to right, and each time you encounter a ground level. Iterate to the left to find the max peak and 
iterate to the right to find the max peak.

Store the maxpeak as you traverse the array.


### Q2: Shopee Network
O(n^2) time | O(n) space, where n is the number of nodes in the network
For each of the nodes in the network, find the path to all the nodes in the graph. 
Note that there shouldn't be any occurences of cycles because for N-1 edges and a connected graph of N vertices, it is not possible 
to have a cycle. So nodes that have already been discovered should not be rediscovered again in a breadth first search from the 
source vertex. 

Breadth First Search from the src vertex would take O(n) time, and since we repeat this for every node in the network, the inefficient
solution would hence be O(n^2) time.


### Q3: Connectivity
O(QN + Q^2) time | O(Q) space -where Q is the number of scenarios and N is the number of switches in the graph.
This implementation basically uses an adjacency list to model the graph network. Each time a "PUSH" operation is seen, add an edge between {1,2}
This method then uses Breath First Search to deduce the number of connected components in the graph. Each time a query is added.

Technically, do you think this BFS is necessary? Some context is that we know for sure that the graph starts out with no connections, and we add edges and we remove edges according to the query. Could we potentially cache the number of CCs and increase and decrease by 1 when we deduce that the number of CCs decreases?

### Q4: Wifi Network
O(EQ) time - where Q is the length of queries and N is the number of engineers. 
For every engineer, compute their pythagorean distance to both base stations (AirFi and GeoFi), since the location of each base station will not change. Then, for every range of the base stations, see which engineers have ranges that lie in both stations, one station and no stations. Tally that number accordingly. 

O(EQ) works, and it has a decent runtime for the size of the input, but I think this is a little too easy for Q4. 

I tried (SEE BRANCH Q4-BST) to model the relationship between Engineer locations using a BST, this couldn't work because I couldn't adapt it to the logic that this engineer has to be in AirFi and GeoFi but not both. I could use a BST to handle the ranges of this engineer to say that its value is larger than the specified range, but not able to identify that this is the same engineer that I am considering. What do you think? 
