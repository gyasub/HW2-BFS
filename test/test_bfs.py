# write tests for bfs
import pytest
from search import graph
import networkx as nx


def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    
    '''
    BFS is a graph traversal algorithm that explores a graph level by level. 
    It starts from a specified source node and explores all the neighboring nodes at the present depth prior to moving on to nodes at the next depth level. 
    BFS is often used to find the shortest path from the source node to all other nodes in an unweighted graph.

    '''

    #instance of the test graph
    graph_instance = graph.Graph('data/tiny_network.adjlist')

    #choosing a start node
    source_node = list(graph_instance.graph.nodes())[0]
    #target_node = list(graph_instance.graph.nodes())[1]

    #getting number of nodes from networkx
    number_of_nodes = graph_instance.graph.number_of_nodes()

    #use my bfs function for traversal without end node
    traverse_result = graph_instance.bfs(start = source_node, end =None)
    
    #asserting that my bfs traverses all the nodes in the graph
    assert len(traverse_result) == number_of_nodes
    


#############################################################################
    
    #introducing a self-made test graph

    test_graph_instance = graph.Graph('data/order_network.adjlist')

    correct_order = ['1','2', '3', '4', '5', '6']

    test_traverse_result = test_graph_instance.bfs(start = '1', end=None)

    #testing for correct order for bfs
    assert test_traverse_result == correct_order


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    #testing the bigger network
    graph_instance = graph.Graph('data/citation_network.adjlist')

   

    #getting one shortest path from networkx function
    shortest_paths = list(nx.all_shortest_paths(graph_instance.graph, source= 'Atul Butte', target= 'Steven Altschuler'))[0]

    traverse_result = graph_instance.bfs(start= 'Atul Butte', end= 'Steven Altschuler')

    #asserting that my bfs yields the shortest path
    assert traverse_result == shortest_paths

#################################
    
    #showing that my bfs yields None if start node does not exist
    traverse_result = graph_instance.bfs(start= 'Gyasu', end=None)
    assert traverse_result == None


    #showing that my bfs yields None if END node does not exist
    traverse_result = graph_instance.bfs(start= 'Atul Butte', end='Bajracharya')
    assert traverse_result == None

#################################

    #raising exception that graph is unconnected
     
    #choosing unconnected source and target nodes 
    source_node = list(graph_instance.graph.nodes())[253]
    target_node = list(graph_instance.graph.nodes())[234]
    
    #traverse bfs
    traverse_result = graph_instance.bfs(start= source_node, end= target_node)
    
    #raising exception for unconnected graph
    with pytest.raises(AssertionError, match="Start and End Nodes are not connected"):
        assert traverse_result != None, "Start and End Nodes are not connected"
