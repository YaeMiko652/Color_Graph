from graph import create_graph
from greedy_edge_color import greedy_edge_coloring
from visualize import visualize_edge_coloring
from get_input import input_int
import networkx as nx

# promt user to choose option
def main():
    print("Wellcome to Graph Coloring Problem")
    while(True):
        print("________________________________________")
        print("1. User input graph")
        print("2. Demo graph")
        print("3. Exit")
        choice = input_int("Please choose your option: ")
        # switch case
        if choice == 1:
            G = create_graph()
            C, max_color = greedy_edge_coloring(G)
            visualize_edge_coloring(G, C, max_color)
        elif choice == 2:
            G = nx.Graph()
            G.add_nodes_from(['D','C', 'A', 'B'])
            G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('A', 'D')])
            C, max_color = greedy_edge_coloring(G)
            visualize_edge_coloring(G, C, max_color)
        elif choice == 3:
            print("Thank you for using our program!!༼ つ ◕_◕ ༽つ")
            break

if __name__=="__main__":
    main()