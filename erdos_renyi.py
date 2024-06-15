import networkx as nx
import matplotlib.pyplot as plt
import random


# Erdos Renyi (n, p) model
def generate_erdos_renyi(n, p):
    G = nx.Graph()
    nodes = list(range(n))
    G.add_nodes_from(nodes)
    for i in nodes:
        for j in range(i + 1, n):
            if random.random() < p:
                G.add_edge(i, j)
    nx.draw(G, with_labels=True)
    print("--------------------------")
    print("Erdos Renyi for", n, "nodes")
    print("--------------------------")
    edge_list = list(G.edges())
    print(edge_list)
    print()
    adjacency_matrix = nx.adjacency_matrix(G)
    print(adjacency_matrix.todense())
    plt.show()


# Erdos Renyi (n, m) model
def generate_erdos_renyi_2(n, m):
    G = nx.Graph()
    nodes = list(range(n))
    G.add_nodes_from(nodes)
    edges = 0
    while edges < m:
        i = random.choice(nodes)
        j = random.choice(nodes)
        if i != j and not G.has_edge(i, j):
            G.add_edge(i, j)
            edges += 1
    nx.draw(G, with_labels=True)
    print("--------------------------")
    print("Erdos Renyi for", n, "nodes and", m, "edges")
    print("--------------------------")
    edge_list = list(G.edges())
    print(edge_list)
    print()
    adjacency_matrix = nx.adjacency_matrix(G)
    print(adjacency_matrix.todense())
    plt.show()


generate_erdos_renyi(10, 0.3)
generate_erdos_renyi_2(10, 20)
