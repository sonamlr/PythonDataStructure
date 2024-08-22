class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_metrix = [[0]*vno for e in range(vno)]
    def add_edge(self, v, u, weight=1):
        if 0<=v<self.vertex_count and 0<=u<self.vertex_count:
            self.adj_metrix[u][v] = weight
            self.adj_metrix[v][u] = weight

        else:
            print("Invalid Vertex")
    def remove_edge(self, u, v):
        if 0<=v<self.vertex_count and 0<=u<self.vertex_count:
            self.adj_metrix[u][v] = 0
            self.adj_metrix[v][u] = 0
        else:
            print("Invalid Vertex")
    def has_edge(self,u,v):
        if 0<=v<self.vertex_count and 0<=u<self.vertex_count:
            return self.adj_metrix[u][v] != 0
        else:
            print("Invalid Vertex")
    def print_adj_metrix(self):
        for row_list in self.adj_metrix:
            print(' '.join(map(str, row_list)))
