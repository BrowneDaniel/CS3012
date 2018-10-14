# adapted from approach found at https://github.com/neasatang/
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

    # wrapper for finding LCA using DFS
    def LCA_DFS_Wrapper(self, graph, nodeA, nodeB):
        global node_A_list
        node_A_list = []
        global node_B_list
        node_B_list = []

        # gets the node routes for each node and stores them in a list
        for node in graph:
            self.LCA_DFS([node], graph, node, 1, nodeA)
            self.LCA_DFS([node], graph, node, 2, nodeB)

        lowest_count = sys.maxsize
        for itemA in node_A_list:
            for itemB in node_B_list:
                for index, node1 in enumerate(reversed(itemA)):
                    count = index
                    for node2 in reversed(itemB):
                        if node1 == node2 and count < lowest_count:  # LCA is the one with the lowest count
                            LCANode = node2
                            return LCANode

                        count += 1

    # calculates the DFS for an LCA node
    def LCA_DFS(self, node_list, graph, node, index, end_node):
        if node == end_node:

            # distinguish between the two routes using index
            if index == 1:
                node_A_list.append(node_list[:])
            elif index == 2:
                node_B_list.append(node_list[:])
            return True

        if not graph[node]:
            return True

        else:
            for child in graph[node]:
                if child not in node_list:
                    node_list.append(child)
                    if not self.LCA_DFS(node_list, graph, child, index, end_node):
                        return False
                    node_list.remove(child)
                else:
                    return False
            return True
