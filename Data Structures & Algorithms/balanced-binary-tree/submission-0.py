# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root) -> int:
        if not root: 
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        return 1 + max(l, r)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        def dfs(root):
            if not root:
                return True
            l = self.helper(root.left)
            r = self.helper(root.right)
            return abs(r - l) <= 1 and dfs(root.left) and dfs(root.right)
        return dfs(root)


