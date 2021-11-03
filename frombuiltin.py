import matplotlib.pyplot as plt
from igraph import Graph, plot

'''
روش دوم
استفاده از دیتاست توکار igraph
'''
g = Graph.Read_GraphML("zachary.graphml")
layout = g.layout("kk")
fig, ax = plt.subplots()
plot(g, layout=layout, bbox=(300, 300), target=ax)
# plt.savefig("builtin.svg")
plt.show()