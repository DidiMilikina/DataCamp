'''
MatrixPlot
Let's now practice making some visualizations. The first one will be the MatrixPlot. In a MatrixPlot, the matrix is the representation of the edges.

Instructions
100 XP
Make a MatrixPlot visualization of the largest connected component subgraph, with authors grouped by their user group number.
First, calculate the largest connected component subgraph by using the nx.connected_component_subgraphs(G) inside the provided sorted() function. Python's built-in sorted() function takes an iterable and returns a sorted list (in ascending order, by default). Therefore, to access the largest connected component subgraph, the statement is sliced with [-1].
Create the MatrixPlot object h. You have to specify the parameters graph and node_grouping to be the largest connected component subgraph and 'grouping', respectively.
Draw the MatrixPlot object to the screen and display the plot.
'''
SOLUTION
# Import necessary modules
from nxviz import MatrixPlot
import matplotlib.pyplot as plt

# Calculate the largest connected component subgraph: largest_ccs
largest_ccs = sorted(nx.connected_component_subgraphs(G), key=lambda x: len(x))[-1]

# Create the customized MatrixPlot object: h
h = MatrixPlot(graph=largest_ccs, node_grouping='grouping')

# Draw the MatrixPlot to the screen
h.draw()
plt.show()