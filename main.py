'''
روش اول
خواندن از فایل zachary

ساختن گره در igraph از صفر شروع می شود
شماره نودها در دیتاست از یک شروع می شود
'''
import matplotlib.pyplot as plt
from igraph import Graph, plot


edges = []
vertices = 0
with open("out.ucidata-zachary", 'r') as f:
    lines = f.readlines()[2:]
    pure_edges = [tuple(x.split()) for x in lines]
    pure_edges_int = list(
        map(lambda x: (int(x[0]), int(x[1])), pure_edges)
    )
    vertices = max([
        max([x[0] for x in pure_edges_int]),
         max([x[1] for x in pure_edges_int])
    ])
    edges = [(x[0] - 1, x[1] - 1) for x in pure_edges_int]

g = Graph()
g.add_vertices(vertices)
g.add_edges(edges)
# print(g.summary())
layout = g.layout("kk")
fig, ax = plt.subplots()
plot(g, layout=layout, bbox=(300, 300), target=ax)
plt.savefig("dataset.svg")


