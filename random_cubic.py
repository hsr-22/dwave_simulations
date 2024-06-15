import networkx as nx
import matplotlib.pyplot as plt
import random


def generate_random_cubic(n):
    G = nx.Graph()
    nodes = list(range(n))
    G.add_nodes_from(nodes)
    for node in nodes:
        while len(G.edges(node)) < 3:
            neighbor = random.choice(nodes)
            if neighbor != node and len(G.edges(neighbor)) < 3:
                G.add_edge(node, neighbor)
    nx.draw(G, with_labels=True)
    print("--------------------------")
    print("Random Cubic for", n, "nodes")
    print("--------------------------")
    edge_list = list(G.edges())
    print(edge_list)
    print()
    adjacency_matrix = nx.adjacency_matrix(G)
    print(adjacency_matrix.todense())
    plt.show()


# for i in range(4, 12, 2):
#     generate_random_cubic(i)
generate_random_cubic(8)
