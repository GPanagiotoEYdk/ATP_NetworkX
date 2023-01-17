import pandas as pd
import numpy as np
import math
import networkx as nx

def NodesCreation(ids, label):
    '''
    creating the dictionary which will be used for adding the related nodes
    
    ids: the columns which will be used as attributes
    label: the node's label 
    
    '''
    d = {'id': ids, 'label': [label]*len(ids)}
    df = pd.DataFrame(d)
    df.set_index('id', inplace=True)
    dictio = df.to_dict(orient='index')
    
    return dictio


def AddSimpleEdge(df, columns, graph, label, subattr):
    '''
    adding an edge between two columns

    df: dataframe to use for selecting the data
    columns: the columns for the edge
    graph: the graph name
    label: the label of the edge added as attribute

    '''
    d = dict(zip(df[columns[0]], df[columns[1]]))

    if subattr == False:
        for k, v in d.items():
            graph.add_edges_from(([(k, v)]), label= label)
    else:
        for k, v in d.items():
            graph.add_edges_from(([(k, t) for t in v]), label= label)
    return d



def NewColumn(x):
    '''
    creating a new column in dataframe based on others
    
    x: dataframe's row
    '''
    a = [i if i else None for i in x]
    b = [item for item in a if not(type(item)==float and (math.isnan(item)) == True)]

    return b

def EdgesView(graph,nodes):
    '''
    searching and presenting the Edges of a node in graph

    graph: the graph network
    nodes: the nodes of the graph to search the edges for

    '''
    d1 = {}
    for i in nodes:
        d2 = {}
        for k1,v1 in graph[i].items():
            for k2,v2 in v1.items():
                d3 = {}
                for k3, v3 in v2.items():
                    d3[k3] = v3
            d2[k1] = d3
        d1[i] = dict(d2)

    return d1
