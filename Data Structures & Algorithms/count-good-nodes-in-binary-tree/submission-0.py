# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        def dfs(root, v):
            if not root:
                return
            if root.val >= v:
                res.append(root.val)
            dfs(root.left, max(root.val, v));
            dfs(root.right, max(root.val, v));
        dfs(root, root.val)
        return len(res)