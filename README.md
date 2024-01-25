![BuildStatus](https://github.com/gyasub/HW2-BFS/workflows/Pytest/badge.svg?event=push)

# Assignment 2

Breadth-first search
Introduction

This Python code defines a Graph class that encapsulates a directed graph using the NetworkX library. The class includes a Breadth-First Search (BFS) function for traversal and pathfinding within the graph.

Class Initialization
The Graph class is initialized with the filename of an adjacency list, read using NetworkX's read_adjlist function. The delimiter for the adjacency list is set to ";".

BFS Method
The core of the code is the bfs method, which performs BFS traversal and pathfinding on the graph.

Method Signature
The bfs method performs a breadth-first traversal and pathfinding on the graph. It returns a list of nodes with the order of BFS traversal when there is no end node input. If an end node is specified and a path exists, it returns a list of nodes with the order of the shortest path. If an end node is specified, and no path exists, it returns None.

Edge Cases Handling
The method handles edge cases such as start being None, the graph being None, or the starting node not being in the graph. It also checks if end is provided and if it exists in the graph. Additionally, it handles the case where start is equal to end, indicating a trivial path.

BFS Implementation
The BFS algorithm is implemented using a queue and a list to keep track of visited nodes. A temporary path list is used to store child-parent relationships during traversal. The algorithm explores nodes level by level, enqueuing neighbors and updating the visited and path lists accordingly.

Pathfinding
If an end node is provided, the algorithm reconstructs the shortest path from start to end using the temporary path list. The path is then returned in reverse order.

Result Handling
The method returns the result based on the input parameters. If end is None, it returns a list of visited nodes in the order of BFS traversal. If a valid end node is provided, it returns the shortest path from start to end. If no path exists for the provided end node, it returns None.