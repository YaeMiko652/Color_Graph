from get_input import input_int, check_input_name_vertices_in_graph
import networkx as nx

# Define a function that takes no input and returns a graph defined by the user
def create_graph():
    # Initialize an empty graph using networkx library
    #M = Graph()
    G = nx.Graph()
    # Ask the user how many num_vertices they want to add
    num_vertices = input_int("How many num_vertices do you want to add? ")
            
    # Loop through num_vertices times and ask the user for the name of each vertex and add it to G
    for i in range(1, num_vertices+1):
        name = check_input_name_vertices_in_graph(G.nodes(), "Enter the name of vertex " + str(i) + ": ")
        G.add_node(name)
        print("Added vertex", name)
    
    # Ask the user how many edges they want to add
    num_edges = input_int(f"How many edges do you want to add?(0 -> {int(num_vertices * (num_vertices-1)/2)}) ")

    # Check if edges is valid (not negative or too large)
    while num_edges < 0 or num_edges > num_vertices*(num_vertices-1)/2:
        if num_edges < 0:
            print("Invalid number of edges. Please enter a non-negative integer.")
        elif num_edges > num_vertices*(num_vertices-1)/2:
            print("Invalid number of edges. Please enter an integer at most", int(num_vertices*(num_vertices-1)/2))
        # Ask the user to enter again
        num_edges = input_int(f"How many edges do you want to add?(0 -> {int(num_vertices * (num_vertices-1)/2)}) ")

    # Loop through edges times and ask the user for the names of the endpoints of each edge and add it to G
    for j in range(1, num_edges+1):
        u, v = input("Enter the names of the endpoints of edge " +
                     str(j)+": ").split()
        
        # Check if u and v are valid (exist in G and not equal)
        # while u not in G.nodes() or v not in G.nodes() or u == v:
        while u not in G.nodes() or v not in G.nodes():
            if u not in G.nodes():
                print("Invalid endpoint. Vertex", u, "does not exist.")
            elif v not in G.nodes():
                print("Invalid endpoint. Vertex", v, "does not exist.")
            elif u == v:
                print("Invalid endpoint. Vertex", u,
                      "cannot be adjacent to itself.")
            # Ask the user to enter again
            u, v = input(
                "Enter the names of the endpoints of edge "+str(j)+": ").split()

        G.add_edge(u, v)
        print("Added edge", u, v)

    # Return the graph G
    return G