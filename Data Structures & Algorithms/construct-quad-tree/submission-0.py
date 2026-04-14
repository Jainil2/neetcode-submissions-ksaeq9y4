"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def all_same(self, matrix):
        first = matrix[0][0]
        return all(cell == first for row in matrix for cell in row)

    def build(self, grid):
        if self.all_same(grid):
            return Node(grid[0][0], True, None, None, None, None)

        n = len(grid)
        h = n // 2

        return Node(
            1,
            False,
            self.build([row[:h] for row in grid[:h]]),
            self.build([row[h:] for row in grid[:h]]),
            self.build([row[:h] for row in grid[h:]]),
            self.build([row[h:] for row in grid[h:]])
        )

    def construct(self, grid):
        return self.build(grid)
