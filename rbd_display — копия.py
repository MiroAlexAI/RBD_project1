import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

def display_graph(graph, reliability):
    pos = left_to_right_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight="bold", arrows=True)
    labels = nx.get_node_attributes(graph, 'reliability')
    nx.draw_networkx_edge_labels(graph, pos)
    nx.draw_networkx_labels(graph, pos, labels={k: f"{k}\n({v:.2f})" for k, v in labels.items()}, font_size=10)
    plt.show()

def left_to_right_layout(graph):
    pos = {}
    levels = list(nx.topological_sort(graph))
    level_dict = defaultdict(int)

    for i, node in enumerate(levels):
        level = len(nx.ancestors(graph, node))
        pos[node] = (level, level_dict[level])
        level_dict[level] += 1

    return pos
