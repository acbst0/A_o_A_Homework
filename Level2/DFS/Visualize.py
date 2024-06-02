# --------------------------------------------------------------------
# I found this code on web. You can visulize this graph with this code
# --------------------------------------------------------------------

import networkx as nx
# pip install networkx
import matplotlib.pyplot as plt
# pip install matplotlib

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = nx.DiGraph(graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=20, font_weight="bold", arrowsize=20)
labels = {edge: edge[-1] for edge in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Graph Visualization")
plt.show()

