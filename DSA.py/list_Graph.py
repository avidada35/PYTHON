class graph:

    def __init__(self,node):
        self.vertex_count = node
        self.adj_list = { V : [] for V in range(node)}

    def add_edge(self, start, end):

        if 0 <= start < self.vertex_count and 0 <= end < self.vertex_count:
            if end not in self.adj_list[start]:
                self.adj_list[start].append(end)
            if start not in self.adj_list[end]:
                self.adj_list[end].append(start)

        else:
            print('Invalid vertex...')


    def has_edge(self,start,end):
        if 0 <= start < self.vertex_count and 0 <= end < self.vertex_count:
            return any(vertex == end for vertex, x in self.adj_list[start])
        else:
            print("Invalid edge...")


    def printing(self):
        for vertex, n in self.adj_list.items():
            print("Node",vertex, ":", n)



p = graph(5)
p.add_edge(0,1)
p.add_edge(1,2)
p.add_edge(1,3)
p.add_edge(2,3)
p.add_edge(3,4)

p.printing()
