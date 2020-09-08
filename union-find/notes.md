# Notes on Union Find Workshop

**Topic: Union Find
Date: 9/6/20
Link: https://fellows.pathrise.com/knowledge/workshops/unionfind
Mentor: Nil Mamano**

## Introduction

### Set Theory
* Set: collection of 0 or more elements
* Subset of set: contains some elements of that set
* 2 disjoint sets contain 0 elements in common
* Partition of set: dividing set into disjoint, non-empty subsets

### Union Find
* Union find: data structure that represents partition of set w/ elements {0, 1, 2, ..., n-1}
* Starts w/ partition of singleton sets: { {0}, {1}, {2}, ..., {n-1} }
* Merge singleton sets together into 2-element sets, then 3-element sets, and so on

### Context
* Used in Kruskal's Minimum Spanning Tree algorithm
* Also called "Disjoint Sets"

### Union and Find operations
* `union(i, j)`: merge elements of subsets i and j together into 1 subset
* `find(i)`: find subset containing element i

## Implementation

### Implementation basics
TODO

### Naive Implementation
TODO

### Better Idea
* Use forrest of trees to represent partition
  * Each tree = subset
  * Root = identifies subset uniquely
* Example:
  * Partition: { {0, 1, 2, 8}, {3, 4, 5, 6, 7, 9} }
  * Forrest (2 trees):
              1                  4
            /   \              /   \
           0     8            5     3
                /                /  |  \
               2                6   7   9
* `union(0, 6)`
  1. Call `find` to find root of 0 and root of 6
  2. Make 1 subtree the child of the other subtree's root
  Try to keep the tree balanced!

### Implementation
* Initially each element is their own parent (so we can tell which node is root)
* Parent pointer points to self
* As the tree grows in size, adjust pointers appropriately
* >>> SEE CODE >>> UF.py

### Optimization #1: Path Compression
* To make the `find()` faster, we can make all nodes in the path point directly to root
  * So that future calls to nodes along the path are O(1)
* `Find()` needs more code for 2nd pass to update parents pointers
* >>> SEE CODE >>> UF.py

### Optimization #2: Union by Size
* When merging subsets together, change the root of the smaller subset and point it to the larger subset
* Example: subset(5) becomes child of root of subset(1) since subset(5) is smaller tree
        1  < - - - - -           
      /   \            5
     4     7         /   \
   /  \   /         3     2
  9   11  10

### Complexity Analysis
* Union-find takes O(n) space (track parent pointers)
* Takes O(\alpha(n)) time (both `union` and `find` operations)
  * inverse ackerman function
  * grows very slowly (basically constant, better than log)
* Without the path compression (optimization #2), complexity is O(log(n)) time

### Variation
* Can also use hashtable / dictionary to store parent pointers
  * Slightly less space efficient but asymptomically the same (O(n))

## PRACTICE
1. Question #1: Social Networks
Given a social network w/ `n` people of ids 0, 1, 2, ..., n-1
List of pairs [id1, id2] denoting friends
Return list index where each person is connected to every other person (forms a path of friends)
Return -1 if not all friends are connected

* Clarification: not a connected components questions, because you have to know the index where everyone is connected

* Example: n=6
[0, 1] [3, 4] [2, 3] [1, 5] [2, 4] [0, 3] [1, 2] [4, 5]

* Approach
  1. Make graph w/ connections
  2. Start at 1 node and see if you can travel to every other node

1. Question #2: Client Records
Company has n client records, each contains list of > 1 emails
2 records belong the same client if they have the same email
Example:
Input: { [a],     
  [b],
  [c, a],   <-- same client as [a]
  [d, c],   <-- same client as [c, a] and [a]
  [e, f, g] }
Output: 3 clients

* Solution:
  * Union all client records
  * Count # subsets

### Practice Questions
>>> SEE SLIDES >>> 
