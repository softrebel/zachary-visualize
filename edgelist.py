import matplotlib.pyplot as plt
from igraph import Graph, plot
g = Graph.Read_Edgelist("edgelist.txt")
layout = g.layout("kk")
fig, ax = plt.subplots()
plot(g, layout=layout, bbox=(300, 300), target=ax)
plt.savefig("from_edge_list.svg")