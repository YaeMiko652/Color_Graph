import networkx as nx
import matplotlib.pyplot as plt
# Define a function that takes a graph G and an edge coloring C and visualizes them using networkx library

colors_list = ["purple", "red", "green", "orange", "blue", "yellow", "pink", "brown", "gray", "olive"]
len_colors = len(colors_list)

def visualize_edge_coloring(G, colors, max_colors):

    if max_colors > len_colors:
        print("There is not enough colors to visualize. Please try again with a smaller graph.")
        return 
    # Create a list of edge colors based on C
    edge_colors = [colors[e] for e in G.edges()] # G.edges() = [(u, v), (u, v), ...], colors = {(u, v): color} color[(u, v)] = color

    # Draw the graph with networkx using spring layout and customizing node size and width
    nx.draw(G,
            # is a layout algorithm that positions nodes on a 2D plane
            pos=nx.shell_layout(G),
            node_size=500,
            width=3,
            with_labels=True,
            font_size=15,
            font_weight='bold',
            edge_color = [colors_list[i-1] for i in edge_colors]
            )
            # edge_cmap=cmap) # cmap is a colormap instance that maps scalar data to colors
    plt.show()