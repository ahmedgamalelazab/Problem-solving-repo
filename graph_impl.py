"""
    Writing graph implementaiton
    we will do it using map data structure
    the verticies will be connected with each others using list
    the nodes will be represented in a string, ["A","B","C","D"]
"""

from queue import Queue


class Graph():
    def __init__(self, nodes:list[str]):
        self.repository = {}
        for node in nodes:
            self.repository[node] = []
        
    def get_vertex_neighbours(self, source) -> list[str]:
        return self.repository[source]        

    def add_neighbour(self, source, destination):
        # warning you can circle yourself
        self.repository[source].append(destination)

    def print_graph(self):
        for node in self.repository:
            print(node, "->", self.repository[node])
            
            

def breadth_first_search(graph: Graph, source:str) -> list[str]:
    q = Queue()
    visited = {}
    results = []
    q.put(source) # enqueue

    while not q.empty():
        vertex = q.get()
        if not vertex in visited:
            visited[vertex] = True
            results.append(vertex)
            if graph.get_vertex_neighbours(vertex) and len(graph.get_vertex_neighbours(vertex)) > 0:
                for neighbour in  graph.get_vertex_neighbours(vertex):
                    q.put(neighbour)
        else:
            continue
    
    return results


if __name__ == "__main__":
    g = Graph(["A","B","C","D","E"])
    
    g.add_neighbour("A","B")
    g.add_neighbour("A","C")
    g.add_neighbour("B","D")
    g.add_neighbour("C","D")
    g.add_neighbour("D","E")
    
    g.print_graph()
    
    output = breadth_first_search(g,"A")
    
    print(output)
    
    