import sys


class DAG(object):

    def __init__(self):
        self.creategraph()

    def creategraph(self):
        self.graph = {}

    def add_node(self, node, graph=None):
        if not graph:
            graph = self.graph

        if node in graph:
            return False

        graph[node] = []

    def add_edge(self, ind_node, dep_node, graph=None):
        if not graph:
            graph = self.graph

        # if both nodes exist in the graph
        if ind_node in graph and dep_node in graph:
            graph[ind_node].append(dep_node)
        else:
            raise KeyError("One or both nodes do not exist")

        def DFS(self, node_list, graph, node):
            if not graph[node]:
                return True
            else:
                for child in graph[node]:
                    if child not in node_list:
                        node_list.append(child)  # Add to list that stores the route
                        if not self.DFS(node_list, graph, child):
                            return False
                        node_list.remove(child)
                    else:
                        return False
                return True

            # wrapper for DFS function

        def DFSWrapper(self, graph):
            result = True
            for node in graph:
                if not self.DFS([node], graph, node):
                    result = False
                    break

            return result
