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
