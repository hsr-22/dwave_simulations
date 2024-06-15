import networkx as nx
import matplotlib.pyplot as plt


def generate_mobius_ladder(n):
    G = nx.Graph()
    nodes = list(range(n))
    G.add_nodes_from(nodes)
    G.add_edges_from([(i, (i + 1) % n) for i in nodes])
    G.add_edges_from([(i, (i + n / 2) % n) for i in nodes])
    nx.draw(G, with_labels=True)
    print("--------------------------")
    print("Mobius Ladder for", n, "nodes")
    print("--------------------------")
    edge_list = list(G.edges())
    print(edge_list)
    print()
    adjacency_list = nx.to_dict_of_lists(G)
    print(adjacency_list)
    adjacency_matrix = nx.adjacency_matrix(G)
    print(adjacency_matrix.todense())
    plt.show()


# for i in range(4, 22, 2):
#     generate_mobius_ladder(i)
generate_mobius_ladder(4)
