class Graph:
  def __init__(self, num_of_nodes, directed=True):
    self.m_num_of_nodes = num_of_nodes
    self.m_directed = directed
    self.m_list_of_edges = []
	
  def add_edge(self, node1, node2, weight=1):        
    self.m_list_of_edges.append([node1, node2, weight])
    if not self.m_directed:
      self.m_list_of_edges.append([node1, node2, weight])

  def print_edge_list(self):
    num_of_edges = len(self.m_list_of_edges)
    for i in range(num_of_edges):
      print("edge", i+1, ":", self.m_list_of_edges[i])

graph = Graph(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_edge_list()