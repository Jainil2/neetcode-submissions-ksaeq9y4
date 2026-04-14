# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return (0, 0)  # (rob, skip)

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        rob = root.val + left[1] + right[1]
        skip = max(left) + max(right)

        return (rob, skip)

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))