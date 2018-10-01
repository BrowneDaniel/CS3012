# Lowest Common Ancestor in a Binary Tree
# Code replicated from method outlined at https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None