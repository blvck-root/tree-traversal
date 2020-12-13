"""
This program implements the breadth-first and depth-first tree search algorithms.
"""

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(self.label)

    # TODO: pretty-print

    def is_leaf(self):
        return not self.branches

def bfs_traversal(tree):
    """Return nodes visited in order.

    Uses the breadth-first search algorithm to traverse a tree set.
    """
    def one_level(t, k):
        """Return the node values of a tree at level k."""
        if k == 0:
            return [t.label]
        labels = []
        for b in t.branches:
            labels += one_level(b, k - 1)
        return labels

    count = 0
    next_level = one_level(tree, 0)
    level_order = []

    while next_level:
        level_order += next_level
        count += 1
        next_level = one_level(tree, count)
    return level_order

def dfs_traversal(tree):
    """Return nodes visited in order.

    Uses the depth-first search algorithm to traverse a tree set.
    """
    if tree.is_leaf():
        return [tree.label]

    traversal = []
    for branch in tree.branches:
        traversal += dfs_traversal(branch)
    return [tree.label] + traversal


example = Tree('A',
               [Tree('B',
                     [Tree('E'),
                      Tree('F')]),
                Tree('C',
                     [Tree('G'),
                      Tree('H')]),
                Tree('D')])

print('Depth First:   {0}'.format(dfs_traversal(example)))
print('Breadth First: {0}'.format(bfs_traversal(example)))
