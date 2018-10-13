from CS3012 import DAG
import unittest

testdag = None

class CS3012test(unittest.TestCase):


    # test adding a node
    def test_add(self):
        global testdag
        testdag = DAG()
        testdag.add_node('A')
        self.assertTrue(testdag.graph == {'A': []})

    # test adding a non-existent node
    def test_add_nonex(self):
        testdag = DAG()
        testdag.add_node('B')
        self.assertFalse(testdag.graph == {'A': []})

    # test adding a duplicate node
    def test_add_dupe(self):
        self.assertFalse(testdag.add_node('A'))

    # test DFS_Wrapper and DFS (returns false if contains cycles):
    def test_wrapf(self):
        testdag = DAG()
        testdag.add_node('A')
        testdag.add_node('B')
        testdag.add_edge('A', 'B')
        testdag.add_node('C')
        testdag.add_node('D')
        testdag.add_edge('B', 'C')
        testdag.add_edge('C', 'A')
        self.assertFalse(testdag.DFSWrapper(testdag.graph))

    # test DFS_Wrapper and DFS (returns true if no cycles)
    def test_wrapt(self):
        testdag = DAG()
        testdag.add_node('B')
        testdag.add_node('C')
        testdag.add_edge('B','C')
        self.assertTrue(testdag)

    # tests for LCA_DFS_Wrapper and LCA_DFS:
    # test for LCA between two nodes in a graph
    def test_LCA(self):
        testdag = DAG()
        testdag.add_node('A')
        testdag.add_node('B')
        testdag.add_node('C')
        testdag.add_node('D')
        testdag.add_node('E')
        testdag.add_node('F')
        testdag.add_node('G')
        testdag.add_edge('A', 'B')
        testdag.add_edge('A', 'C')
        testdag.add_edge('A', 'D')
        testdag.add_edge('B', 'G')
        testdag.add_edge('C', 'E')
        testdag.add_edge('C', 'F')
        testdag.LCA_DFS_Wrapper(testdag.graph, 'G', 'F')
        self.assertTrue(testdag.LCA_DFS_Wrapper(testdag.graph, 'G', 'F') == 'A')

    # test LCA between a node and its parent
    def test_LCA_parent(self):
        testdag = DAG()
        testdag.add_node('A')
        testdag.add_node('B')
        testdag.add_node('C')
        testdag.add_node('D')
        testdag.add_node('E')
        testdag.add_node('F')
        testdag.add_node('G')
        testdag.add_edge('A', 'B')
        testdag.add_edge('A', 'C')
        testdag.add_edge('A', 'D')
        testdag.add_edge('B', 'G')
        testdag.add_edge('C', 'E')
        testdag.add_edge('C', 'F')
        testdag.LCA_DFS_Wrapper(testdag.graph, 'F', 'C')
        self.assertTrue(testdag.LCA_DFS_Wrapper(testdag.graph, 'F', 'C') == 'C')

    # test LCA of a node and a non-existent node
    def test_LCA_nonex(self):
        testdag = DAG()
        testdag.add_node('A')
        testdag.add_node('B')
        testdag.add_edge('A', 'B')
        self.assertTrue(testdag.LCA_DFS_Wrapper(testdag.graph, 'A', 'X') is None)

    # test LCA on an empty graph
    def test_LCA_empty(self):
        testdag = DAG()
        self.assertTrue(testdag.LCA_DFS_Wrapper(testdag.graph, None, None) is None)