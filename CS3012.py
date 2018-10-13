import sys


class DAG(object):

    # create empty set for nodes for the DAG
    def __init__(self):
        self.create_graph()

    # creates empty dict
    def create_graph(self):
        self.graph = {}

    # add node to set
    def add_node(self, node, graph=None):
        if not graph:
            graph = self.graph

        if node in graph:
            return False

        graph[node] = []

    # add edge to set
    def add_edge(self, ind_node, dep_node, graph=None):
        if not graph:
            graph = self.graph