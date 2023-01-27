import pandas as pd
import numpy as np
import math
import networkx as nx
from typing import Callable, Optional, Tuple, Union, List  


def NodesCreation(ids: str, label:str) -> dict:
    '''
    creating the dictionary which will be used for adding the related nodes
    
    Parameters
    ----------
    ids: the columns which will be used as attributes
    label: the node's label 
    '''
    d = {'id': ids, 'label': [label]*len(ids)}
    df = pd.DataFrame(d)
    df.set_index('id', inplace=True)
    dictio = df.to_dict(orient='index')
    
    return dictio


def AddSimpleEdge(df: pd.DataFrame, columns: List, graph: nx.MultiDiGraph, label: str, subattr: bool) -> dict:
    '''
    adding an edge between two columns
    
    Parameters
    ----------
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



def NewColumn(x: pd.Series)-> List:
    '''
    creating a new column in dataframe based on others
    
    Parameters
    ----------
    x: dataframe's row
    '''
    a = [i if i else None for i in x]
    b = [item for item in a if not(type(item)==float and (math.isnan(item)) == True)]

    return b

def EdgesView(graph: nx.MultiDiGraph , nodes: List) -> dict:
    '''
    searching and presenting the Edges of a node in graph

    Parameters
    ----------
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

def GraphQuerying(graph: nx.MultiDiGraph, source:str, target:str, in_between:str) -> List:
    '''
    searching and presenting the target nodes connected to the source node 

    Parameters
    ----------
    graph: the graph network
    source: the node we want to seacrh for its targets, as argument the id
    target: the targeted nodes, as argument the label
    in_between: the node connection of source and targets
    '''

    connection_nodes = [conn_node for conn_node in graph.to_undirected().neighbors(source) if graph.nodes[conn_node]['label'] == in_between]
    
    return [node for conn_node in connection_nodes for node in graph.to_undirected().neighbors(conn_node)  if str(node)[0:4]== target]