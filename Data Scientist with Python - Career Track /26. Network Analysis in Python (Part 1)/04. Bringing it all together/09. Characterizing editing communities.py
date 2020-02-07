'''
Characterizing editing communities
You're now going to combine what you've learned about the BFS algorithm and concept of maximal cliques to visualize the network with an ArcPlot.

The largest maximal clique in the Github user collaboration network has been assigned to the subgraph G_lmc. Note that for NetworkX version 2.x and later, G.subgraph(nodelist) returns only an immutable view on the original graph. We must explicitly ask for a .copy() of the graph to obtain a mutatable version.

Instructions
100 XP
Go out 1 degree of separation from the clique, and add those users to the subgraph. Inside the first for loop:
Add nodes to G_lmc from the neighbors of G using the .add_nodes_from() and .neighbors() methods.
Using the .add_edges_from(), method, add edges to G_lmc between the current node and all its neighbors. To do this, you'll have create a list of tuples using the zip() function consisting of the current node and each of its neighbors. The first argument to zip() should be [node]*len(list(G.neighbors(node))), and the second argument should be the neighbors of node.
Record each node's degree centrality score in its node metadata.
Do this by assigning nx.degree_centrality(G_lmc)[n] to G_lmc.node[n]['degree centrality'] in the second for loop.
Visualize this network with an ArcPlot sorting the nodes by degree centrality (you can do this using the keyword argument node_order='degree centrality').
'''
SOLUTION
# Import necessary modules
from nxviz import ArcPlot
import matplotlib.pyplot as plt

# Identify the largest maximal clique: largest_max_clique
largest_max_clique = set(sorted(nx.find_cliques(G), key=lambda x: len(x))[-1])

# Create a subgraph from the largest_max_clique: G_lmc
G_lmc = G.subgraph(largest_max_clique).copy()  

# Go out 1 degree of separation
for node in list(G_lmc.nodes()):
    G_lmc.add_nodes_from(G.neighbors(node))
    G_lmc.add_edges_from(zip([node]*len(list(G.neighbors(node))), G.neighbors(node)))

# Record each node's degree centrality score
for n in G_lmc.nodes():
    G_lmc.node[n]['degree centrality'] = nx.degree_centrality(G_lmc)[n]

# Create the ArcPlot object: a
a = ArcPlot(graph=G_lmc, node_order='degree centrality')

# Draw the ArcPlot to the screen
a.draw()
plt.show()