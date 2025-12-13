
import sys
import time
import traceback
import matplotlib.pyplot as plt
import networkx as nx
import plotly.graph_objects as go
from pyvis.network import Network
import networkx as nx


def plotly(graph):

    # Convert to networkx
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Get layout
    pos = nx.spring_layout(G, k=0.5, iterations=50)

    # Create edge traces
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(x=edge_x, y=edge_y,
                            mode='lines',
                            line=dict(width=0.5, color='#888'),
                            hoverinfo='none')

    # Create node traces
    node_x, node_y, node_text, node_color = [], [], [], []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)

        if node == 'svr':
            node_color.append('green')
        elif node == 'out':
            node_color.append('red')
        elif node in ['fft', 'dac']:
            node_color.append('yellow')
        else:
            node_color.append('lightblue')

    node_trace = go.Scatter(x=node_x, y=node_y,
                            mode='markers+text',
                            text=node_text,
                            textposition='top center',
                            marker=dict(size=10, color=node_color, line_width=1))

    # Create figure
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=40),
                        xaxis=dict(showgrid=False, zeroline=False,
                                   showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    fig.show()


def simplegraph(graph):
    # Convert to networkx graph
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Highlight special nodes
    node_colors = []
    for node in G.nodes():
        if node == 'svr':
            node_colors.append('green')
        elif node == 'out':
            node_colors.append('red')
        elif node in ['fft', 'dac']:
            node_colors.append('yellow')
        else:
            node_colors.append('lightblue')

    # Draw
    plt.figure(figsize=(16, 12))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos,
            node_color=node_colors,
            node_size=100,
            with_labels=True,
            font_size=6,
            arrowstyle=['->'],
            arrowsize=10,
            edge_color='gray',
            alpha=0.7)

    plt.title(f"Graph: {len(G.nodes())} nodes, {len(G.edges())} edges")
    plt.tight_layout()
    plt.show()


def pyvisplot(graph):
    net = Network(height='1200px', width='1400px',
                  directed=True, notebook=False
                  )

    # Add ALL nodes first
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)

    for node in all_nodes:
        if node == 'you':
            net.add_node(node, label=str(node), color='green', size=48, font={'size': 144})
        elif node == 'out':
            net.add_node(node, label=str(node), color='red', size=48, font={'size': 144})
        elif node == 'svr':
            net.add_node(node, label=str(node), color='blue', size=48, font={'size': 144})
        elif node in ['fft', 'dac']:
            net.add_node(node, label=str(node), color='orange', size=48, font={'size': 144})
        else:
            net.add_node(node, color='#E0E0E0', borderWidth=1,
                         borderWidthSelected=2, borderColor='cyan',
                         size=10
                         )

    # Add edges
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            net.add_edge(node, neighbor)

    net.write_html('graph.html')
    print("Graph saved to graph.html - open in browser")


def process_lines(lines):
    graph = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        node, neighbors = line.split(':')
        graph[node.strip()] = neighbors.strip().split()
    return graph


def main():
    if len(sys.argv) != 2:
        print("Usage: python day11.py <filename>. Using default small")
        # sys.exit(1)
        filename = "input"
    else:
        filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        print(f"Read {len(lines)} lines from {filename}")
        graph = process_lines(lines)
        # print('small  part 1: ANSWER 1')
        # print("Answer part 1: should be", part_1(graph))
        print(f"Total nodes: {len(graph)}")
        print(f"Total edges: {sum(len(v) for v in graph.values())}")
        # print('small  part 2: ANSWER 2')
        # start = time.time()
        # print("Answer part 2: should be", part_2(graph))
        # end = time.time()
        # print(f"Time: {end - start:.3f} seconds")
        # simplegraph(graph)
        # plotly(graph)
        pyvisplot(graph)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
