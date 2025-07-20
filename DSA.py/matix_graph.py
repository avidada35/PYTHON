class graph:
    def __init__(self,edge):
        self.vertex_count = edge
        self.adj_matrix = [ [0]*edge for i in range(edge)]

    def add_edge(self,start,end,wieght=1):
        if 0<=start<self.vertex_count and 0 <= end < self.vertex_count:
            self.adj_matrix[start][end] = wieght
            self.adj_matrix[end][start] = wieght

        else:
            print('Invalid edge...')

    def has_matrix(self,start,end):
        if 0<=start<self.vertex_count and 0<=end<self.vertex_count:
            self.add_edge[start][end] != 0

        else:
            print('Invalid Edge...')


    def printing(self):
        for i in self.adj_matrix:
            print(" ".join(map(str,i)))

p = graph(5)

p.add_edge(0,1)
p.add_edge(1,2)
p.add_edge(1,3)
p.add_edge(2,3)
p.add_edge(3,4)

p.printing()