import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """




        #########EDGE CASES########
        if start is None or self.graph is None or not self.graph.has_node(start):
            return None
        
        if end is not None and not self.graph.has_node(end):
            return None
        
        if start == end:        #if start node and end node are the same
            return None
        ########################





        # initialize the queue
        my_queue = []

        #List of visited nodes; initialized with start node
        visited = [start]

        #created temporary path storing child and parent of each node
        temp_path = []

        
        #add starting node to the queue
        my_queue.append(start)
            

        while my_queue:
            popped_item = my_queue.pop(0)       #remove 0 index from list
            

            if end is not None:
                if popped_item == end:          #if popped item is the end node
                    path = [end]
                    while temp_path:
                        child, parent = temp_path.pop()
                        if child == end:
                            path.append(parent)
                            end = parent
                    
                    path.reverse()              #reverse the path to go from start--> finish

                    return path


            neighbor_nodes = list(self.graph.neighbors(popped_item))        #look at neighbors of the node

            for neighbor in neighbor_nodes:
                if neighbor not in visited:
                    visited.append(neighbor)                                #adding nodes to visited
                    temp_path.append((neighbor, popped_item))
                    my_queue.append(neighbor)

        if end is None:
            return visited                          #return visited when end=None
            
        else:
            return None                             #return None if no path found



                




