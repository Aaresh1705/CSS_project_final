import plotly.graph_objects as go

# 1. Build a sample 3D scatter
fig = go.Figure(
    data=[
        go.Scatter3d(
            x=[1, 2, 3, 4],
            y=[10, 15, 13, 17],
            z=[5, 7, 9, 11],
            mode='markers',
            marker=dict(size=8)
        )
    ],
    layout=go.Layout(
        title="Sample Rotatable 3D Scatter",
        scene=dict(
            xaxis_title='X Axis',
            yaxis_title='Y Axis',
            zaxis_title='Z Axis'
        )
    )
)

# 2. Export to a standalone HTML file under docs/
fig.write_html(
    "docs/rotatable_plot.html",
    include_plotlyjs="cdn"  # loads Plotly.js from the CDN
)

print("Written rotatable_plot.html → docs/rotatable_plot.html")
