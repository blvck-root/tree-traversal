"""
This program implements the breadth-first and depth-first tree search algorithms.
"""

class Tree:
    def __init__(self, node, branches=[]):
        self.node = node
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.node, repr(self.branches))
        else:
            return 'Tree({0})'.format(self.node)

    # TODO: pretty-print

    def is_leaf(self):
        return not self.branches

def bfs_traversal(tree):
    """Return nodes visited in order.

    Uses the breadth-first search algorithm to traverse a tree set.
    """
    # TODO: write bfs code here


def dfs_traversal(tree):
    """Return nodes visited in order.

    Uses the depth-first search algorithm to traverse a tree set.
    """
    if tree.is_leaf():
        return [tree.node]

    traversal = []
    for branch in tree.branches:
        traversal += dfs_traversal(branch)
    return [str(tree.node)] + traversal


example = Tree('A',
               [Tree('B',
                     [Tree('E')]),
                Tree('D'),
                Tree('C',
                     [Tree('F'),
                      Tree('G')])])

print(dfs_traversal(example))
# print(bfs_traversal(example))
