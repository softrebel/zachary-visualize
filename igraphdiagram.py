from igraph import *

g = Graph.Read_GraphML("zachary.graphml")
#same as using layout = g.layout("kk")
layout = g.layout_kamada_kawai()
plot(g, layout=layout).save('igraphdiagram.png')