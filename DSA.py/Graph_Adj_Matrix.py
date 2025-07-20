"""Graph Using Adjecent Matrix"""
class Graph:
    def __init__(self,vxt):
        self.vertex_count = vxt
        self.adj_matrix = [[0]*vxt for i in range(vxt)]
        
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
            
        else:
            print("Invalid Vertex!!")
            
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<vertex_count:
            self.adj_matrix[u][v] = 0
            
        else:
            print("Invalid Vertex!!")
            
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid Vertex!!")
            
    def print_matrix(self):
        for i in self.adj_matrix:
            print("--".join(map(str,i)))
            
            
g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(3,1)
g.add_edge(3,2)
g.add_edge(3,4)
g.print_matrix()
#O/P : 
""" 0--1--0--0--0
    1--0--1--1--0
    0--1--0--1--0
    0--1--1--0--1
    0--0--0--1--0 """
        
            
            
            
            
            
            
            
    