import networkx as nx
import matplotlib.pyplot as plt

cities = []
with open('cities.csv', mode='r') as file:
    for i in file:
        edge1, edge2, dist = i.split(';')
        edge1, edge2, dist = str(edge1), str(edge2), int(dist)
        cities.append([edge1, edge2, dist])
print(cities)

g = nx.Graph()
for edge in cities:
    g.add_edge(edge[0], edge[1], weight=edge[2])

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.show()
