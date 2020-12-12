"""
This program implements the breadth-first and depth-first tree search algorithms.
"""

class Tree:
    def __init__(self, root, branches=[]):
        self.root = root
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.root, repr(self.branches))
        else:
            return 'Tree({0})'.format(self.root)

    # TODO: pretty-print

    def is_leaf(self):
        return not self.branches

def bfs(tree, item):
    """Return search item and nodes visited.

    Uses the breadth-first search algorithm to find an item in the tree set.
    Returns -1 if item not found and a list of all nodes visited before the
    search concluded.
    """
    # TODO: write bfs code here


def dfs(tree, item):
    """Return search item and nodes visited.

    Uses the depth-first search algorithm to find an item in the tree set.
    Returns -1 if item not found and a list of all nodes visited before the
    search concluded.
    """
    # TODO: write dfs code here

