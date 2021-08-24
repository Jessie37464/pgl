#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx # networkx是一个常用的绘制复杂图形的Python包。

def display_graph(g):
    nx_G = nx.Graph()
    nx_G.add_nodes_from(range(g.num_nodes))
    nx_G.add_edges_from(g.edges)

    pos = {0: [0.5, 0.5], 1:[0.6, 0.4], 2:[0.47, 0.67], 3: [0.35, 0.55], 4:[0.4, 0.4], 5:[0.5, 0.3],
           6: [0.8, 0.4], 7:[0.65, 0.65], 8:[0.6, 0.8], 9:[0.45, 0.85], 10:[0.15, 0.7], 11: [0.1, 0.4],
           12:[0.2, 0.2], 13:[0.3, 0.1], 14:[0.55, 0.15], 15:[0.7, 0.22]}
    nx.draw(nx_G, 
            pos,
            with_labels=True,
            node_color='green', 
            edge_color='green',
            node_size=1000)

    plt.show()

#display_graph(g)# 创建一个GraphWrapper作为图数据的容器，用于构建图神经网络。

def display_subgraph(g, sub_nodes, sub_edges):
    nx_G = nx.Graph()
    nx_G.add_nodes_from(range(g.num_nodes))
    nx_G.add_edges_from(g.edges)

    pos = {0: [0.5, 0.5], 1:[0.6, 0.4], 2:[0.47, 0.67], 3: [0.35, 0.55], 4:[0.4, 0.4], 5:[0.5, 0.3],
           6: [0.8, 0.4], 7:[0.65, 0.65], 8:[0.6, 0.8], 9:[0.45, 0.85], 10:[0.15, 0.7], 11: [0.1, 0.4],
           12:[0.2, 0.2], 13:[0.3, 0.1], 14:[0.55, 0.15], 15:[0.7, 0.22]}
    nx.draw(nx_G, 
            pos,
            with_labels=True,
            node_color='green',
            edge_color='green',
            node_size=1000,
            width=1)

    nx.draw_networkx_nodes(nx_G, pos, nodelist=[0], node_color='red', node_size=1000)

    for color, nodes in sub_nodes.items():
        nx.draw_networkx_nodes(nx_G, pos, nodelist=nodes, node_color=color, node_size=1000)

    for color, edges in sub_edges.items():
        nx.draw_networkx_edges(nx_G, pos, edgelist=edges, edge_color=color, width=5)

    plt.show()