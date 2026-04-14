# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, ans):
        if not root:
            return 0
        l = self.dfs(root.left, ans)
        r = self.dfs(root.right, ans)
        ans[0] = max(ans[0], l + r)
        return 1 + max(l, r)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.dfs(root, ans)
        return ans[0]
