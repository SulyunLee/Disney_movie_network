from igraph import *
import argparse
import pandas as pd
import numpy as np
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-filename", help="the name of the csv file with adjacency matrix")
    args = parser.parse_args()

    filename = args.filename

    random.seed(12345)

    adj_filename = "../datasets/{}".format(filename)
    adj = pd.read_csv(adj_filename, index_col=0)

    # convert adjacency matrix file into numpy array
    adj_arr = adj.values

    # node names
    node_name = adj.columns

    # find negative relationships
    neg_indices = np.argwhere(adj_arr == -1)

    # generate graph
    g = Graph.Weighted_Adjacency(adj_arr.tolist(), ADJ_UPPER, attr="weight")
    g.vs["name"] = node_name

    # specify settings for plotting graph
    layout = "fr"
    layout = g.layout(layout) # specify layout
    edge_color_dict = {1:"#1E90FF", -1:"#DC143C"} # set colors depending on edge weight

    visual_style = {}
    visual_style["layout"] = layout
    visual_style["vertex_color"] = "#DCDCDC"
    visual_style["vertex_label"] = g.vs["name"]
    visual_style["vertex_size"] = 30
    visual_style["vertex_label_dist"] = 2
    visual_style["edge_color"] = [edge_color_dict[w] for w in g.es["weight"]]
    visual_style["bbox"] = (700,700)
    visual_style["margin"] = 50
    visual_style["hovermode"] = "closest"

    # plot graph
    plot(g, **visual_style)
    


