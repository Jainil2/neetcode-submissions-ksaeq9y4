# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def dfs(self, root, p):
    if not root:
      return None
    if not root.left and not root.right:
      if root.val == target:
        return None
    root.left = self.dfs(root.left, root)
    root.right = self.dfs(root.right, root)
    if root.val == target and not root.left and not root.right:
      return None
    return root
  def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    return self.dfs(root, None)