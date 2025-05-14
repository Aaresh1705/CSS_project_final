import numpy as np
import pickle
import matplotlib.pyplot as plt
import ast
import pandas as pd
import networkx as nx
from matplotlib.patches import Patch

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

def plotNetwork_color(G):
    #Genre hierarchy
    hierarchy = ["eurovision pop", "jazz", "choral", "classical", "heavy metal", "country", "electronic", "folk" , "pop", "rock"]
    # the hierarchy is defined in a way that the most common genres pop and rock are at the end of the list

    def pick_genre(genres_raw):
        if isinstance(genres_raw, str):
            try:
                genres = ast.literal_eval(genres_raw)
            except (ValueError, SyntaxError):
                genres = []
        else:
            genres = genres_raw or []

        genres_lower = [g.lower().strip() for g in genres]

        for genre in hierarchy:
            if genre in genres_lower:
                return genre
        return "other"


    genre_map = {node: pick_genre(G.nodes[node].get("genre")) for node in G.nodes()}


    unique_genres = sorted(set(genre_map.values()))

    color_map = {genre: plt.cm.tab10(i % 10) for i, genre in enumerate(unique_genres)}

    #NOTE: is the right genre swapped??
    color_map["other"], color_map["jazz"] = color_map["jazz"], color_map["other"]

    node_colors = [color_map[genre_map[node]] for node in G.nodes()]


    # Plot the graph
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 9))

    nx.draw(
        G,
        pos,
        node_color=node_colors,
        with_labels=False,
        node_size=50,
        edge_color='gray'
    )

    # Create a legend as a table
    legend_elements = [Patch(facecolor=color_map[genre], label=genre) for genre in unique_genres]
    plt.legend(handles=legend_elements, title="Genre (Color)", loc="upper right", bbox_to_anchor=(1.15, 1.0))

    plt.title("Network Colored by Representative Genre")
    plt.tight_layout()
    plt.show()