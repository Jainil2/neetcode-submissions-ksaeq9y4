# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, res):
        if not root:
            return 0
        lmax = self.dfs(root.left, res)
        rmax = self.dfs(root.right, res)
        res[0] = max(res[0], lmax + rmax)
        return 1 + max(lmax, rmax)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.dfs(root, res)
        return res[0]
        