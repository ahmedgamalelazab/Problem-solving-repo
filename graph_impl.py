"""
    Writing graph implementaiton
    we will do it using map data structure
    the verticies will be connected with each others using list
    the nodes will be represented in a string, ["A","B","C","D"]
"""

from queue import Queue
from stack_impl_doubly_linked_list_based import Stack

class Graph():
    def __init__(self, nodes:list[str]):
        self.repository = {}
        self.verticies = nodes or []
        for node in nodes:
            self.repository[node] = []
        
    def get_vertex_neighbours(self, source:str) -> list[str]:
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


def depth_first_search(graph: Graph, source:str) -> list[str]:
    stack = Stack()
    visited = {}
    results = []
    stack.push(source)
    
    while not stack.is_empty():
        vertex = stack.pop()
        if not vertex in visited:
            visited[vertex] = True
            results.append(vertex)
            is_vertex_having_neighbours = True if graph.get_vertex_neighbours(source) and len(graph.get_vertex_neighbours(source)) > 0 else False
            if is_vertex_having_neighbours:
                vertex_neighbours = graph.get_vertex_neighbours(vertex)
                for neighbour in vertex_neighbours:
                    stack.push(neighbour) 
            
        else:
            continue
    
    return results


def dfs_rec(g: Graph, vertex: str, visited:dict[str,bool], in_path:dict[str: bool])-> bool:
    if vertex in in_path and in_path[vertex] == True:
        return True
    if vertex in visited:
        return False

    visited[vertex] = True
    in_path[vertex] = True
    
    nbs = g.get_vertex_neighbours(vertex)
    
    for nb in nbs:
        if dfs_rec(g, nb, visited, in_path):
            return True
    
    in_path[vertex] = False # recursion is useful here in order to shutdown the path
    return False

def detect_cycle_in_graph(graph: Graph)-> bool:
    vertices = graph.verticies
    visitied = {}
    in_path = {}
    
    for v in vertices:
        if v not in visitied:
            if dfs_rec(graph, v, visitied, in_path):
                return True
    return False



if __name__ == "__main__":
    g = Graph(["A","B","C","D","E"])
    
    g.add_neighbour("A","B")
    g.add_neighbour("A","C")
    g.add_neighbour("B","D")
    g.add_neighbour("C","D")
    g.add_neighbour("D","E")
    
    g.print_graph()
    
    bfs_output = breadth_first_search(g,"A")
    dfs_output = depth_first_search(g,"A")
    cycle_detected = detect_cycle_in_graph(g)
    
    print("BFS->",bfs_output)
    print("DFS->",dfs_output)
    print("DCIG->",cycle_detected)
    
    