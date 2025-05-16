import pickle
import networkx as nx
import plotly.graph_objects as go

# 1. Load your saved graphs
with open("data/wip/groups_graph.pkl", "rb") as f:
    GroupsG = pickle.load(f)

# 2. Extract the largest connected component
largest_cc = max(nx.connected_components(GroupsG), key=len)
G_sub = GroupsG.subgraph(largest_cc).copy()

# 3. Compute node positions
pos = nx.spring_layout(G_sub, seed=42)

# 4. Build edge traces
edge_x, edge_y = [], []
for u, v in G_sub.edges():
    x0, y0 = pos[u]
    x1, y1 = pos[v]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    mode="lines",
    line=dict(width=1, color="#888"),
    hoverinfo="none"
)

# 5. Build node traces with hover text
node_x, node_y, node_text = [], [], []
for node, data in G_sub.nodes(data=True):
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)

    # Assemble your hover‐text: degree + any attributes
    info = [f"<b>{node}</b>", f"Degree: {G_sub.degree(node)}"]
    for attr, val in data.items():
        info.append(f"{attr}: {val}")
    node_text.append("<br>".join(info))

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode="markers",
    marker=dict(size=10, color="skyblue"),
    text=node_text,
    hoverinfo="text"
)

# 6. Create the figure
fig = go.Figure(
    data=[edge_trace, node_trace],
    layout=go.Layout(
        title="Groups Network (hover nodes for details)",
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        margin=dict(t=50, l=0, r=0, b=0)
    )
)

# 7. Export to a standalone HTML file in docs/
fig.write_html(
    "docs/network.html",
    include_plotlyjs="cdn"
)
print("→ docs/network.html written")
