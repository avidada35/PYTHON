import matplotlib.pyplot as plt
import networkx as nx

# Create the weighted undirected graph (same as the one in the previous Prim's MST solution)
G = nx.Graph()
edges = [
    (1, 2, 28), (1, 6, 10),
    (2, 3, 16), (2, 7, 14),
    (3, 4, 12),
    (4, 5, 22), (4, 7, 18),
    (5, 6, 25),
    (7, 5, 24)
]
G.add_weighted_edges_from(edges)

# Define the MST edges as selected during the Prim's process from vertex 1
mst_edges = [(1, 6), (6, 5), (5, 4), (4, 3), (4, 7), (7, 2)]

# Positions for all nodes for consistent layout
pos = nx.spring_layout(G, seed=42)

# Draw original graph with all weights
plt.figure(figsize=(50, 30))
nx.draw(G, pos, with_labels=True, node_color='blue', edge_color='black', node_size=1000, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Highlight MST edges
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=2, edge_color='green')

plt.title("Step-by-Step Prim's Algorithm MST (Start from Vertex 1)", fontsize=20)
plt.axis('off')
plt.show()
