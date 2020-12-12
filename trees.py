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
