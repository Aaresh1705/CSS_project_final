import numpy as np
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx

def basic_graph_stats(G):
    N = G.number_of_nodes()
    L = G.number_of_edges()

    p = L / ((N*(N-1))/2)  # for undirected graphs, we divide by 2

    k = p*(G.number_of_nodes() - 1)

    print(f"Size of network: {N}")
    print(f"Probability p: {p}")
    print(f"Average degree: {k}")
    return None


# Function to visualize the graph F and G in one figure
def plot_2graphs(G, F):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)

    plt.title("Random Network")
    plt.axis('off')
    pos = nx.spring_layout(F)
    nx.draw(F, pos, node_size=10, node_color='blue', alpha=0.5, width=0.2)
    plt.subplot(1, 2, 2)
    plt.title("Original Network")
    plt.axis('off')
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_size=10, node_color='red', alpha=0.5, width=0.2)
    plt.show()


def scatter_dist(G, F):
    def get_deg_dist(graph):
        degree_dict = dict(graph.degree())
        return np.unique(list(degree_dict.values()), return_counts=True)

    # Get degree distributions
    degs_G, counts_G = get_deg_dist(G)
    degs_F, counts_F = get_deg_dist(F)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(degs_G, counts_G, s=20, alpha=0.7, label='Original Network', color='blue')
    plt.scatter(degs_F, counts_F, s=20, alpha=0.3, label='Random Network', color='red')

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Degree", fontsize=12)
    plt.ylabel("Nodes with degree count", fontsize=12)
    plt.title("Degree Distribution Comparison (Log-Log)", fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.3)
    plt.show()