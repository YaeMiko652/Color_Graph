def greedy_edge_coloring(G):
    # Initialize an empty dictionary to store the colors of each edge
    colors = {} 
    # Initialize a variable to keep track of the maximum color used so far
    max_color = 0
    # Loop through the edges of G in any order
    for u, v in G.edges():  # G.edges() returns a non-duplicated list of edges
        # Initialize an empty set to store the colors of the adjacent edges
        used_colors = set()  # Use set to avoid duplicates
        # Loop through the neighbors of u and v and add their edge colors to used_colors
        for w in G.neighbors(u): # G.neighbors(u) returns a list of neighbors of u
            if (u, w) in colors:
                used_colors.add(colors[(u, w)])
            if (w, u) in colors:
                used_colors.add(colors[(w, u)])
        for w in G.neighbors(v):
            if (v, w) in colors:
                used_colors.add(colors[(v, w)])
            if (w, v) in colors:
                used_colors.add(colors[(w, v)])
        # Find the minimum positive integer that is not in used_colors
        color = 1
        while color in used_colors:
            color += 1
        # Assign this color to the edge (u, v) and update max_color if needed
        colors[(u, v)] = color
        if color > max_color:
            max_color = color
    # Return the dictionary of edge colors and the maximum color used
    print(f"colors {colors}")
    return colors, max_color # colors = {(u, v): color} 