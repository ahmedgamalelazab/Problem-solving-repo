
from graph_impl import Graph, breadth_first_search

sample_nodes = ["A","B","C","D","E","F","G","H"]

def test_breadth_first_search_on_simple_graph():
    sample_graph = Graph(sample_nodes[:])
    
    sample_graph.add_neighbour("A","B")
    sample_graph.add_neighbour("A","C")
    sample_graph.add_neighbour("A","D")
    sample_graph.add_neighbour("A","E")
    sample_graph.add_neighbour("B","F")
    sample_graph.add_neighbour("C","F")
    sample_graph.add_neighbour("D","F")
    sample_graph.add_neighbour("E","F")
    sample_graph.add_neighbour("F","G")
    sample_graph.add_neighbour("F","H")
    sample_graph.add_neighbour("G","H")
    
    
    output = breadth_first_search(sample_graph, "A")
    
    assert output == ["A","B","C","D","E","F","G","H"]


def test_breadth_first_search_on_cycle_graph():
    sample_graph = Graph(sample_nodes[:])
    
    sample_graph.add_neighbour("A","B")
    sample_graph.add_neighbour("A","C")
    sample_graph.add_neighbour("A","D")
    sample_graph.add_neighbour("A","E")
    sample_graph.add_neighbour("B","F")
    sample_graph.add_neighbour("C","F")
    sample_graph.add_neighbour("D","F")
    sample_graph.add_neighbour("E","F")
    sample_graph.add_neighbour("E","A")
    sample_graph.add_neighbour("F","G")
    sample_graph.add_neighbour("F","H")
    sample_graph.add_neighbour("G","H")
    
    
    output = breadth_first_search(sample_graph, "A")
    
    assert output == ["A","B","C","D","E","F","G","H"]
    

