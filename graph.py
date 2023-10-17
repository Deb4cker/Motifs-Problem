import random
import networkx as nx

def generate_tree_with_density(num_nodes, density):
    # Create an empty graph
    G = nx.Graph()

    # Calculate the maximum number of edges for the given density
    max_edges = (num_nodes * (num_nodes - 1) / 2) * density

    # Add nodes to the graph
    G.add_nodes_from(0)

    while G.number_of_edges() < max_edges:
        # Randomly select two distinct nodes
        node1, node2 = random.sample(G.nodes(), 2)

        # Ensure the selected nodes are not already connected
        if not G.has_edge(node1, node2):
            # Add an edge between the two nodes
            G.add_edge(node1, node2)

    return G

