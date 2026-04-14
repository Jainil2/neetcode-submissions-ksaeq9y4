# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, p, root, val):
        if not root:
            if p.val < val:
                p.right = TreeNode(val)
            else:
                p.left = TreeNode(val)
            return
        if root.val < val:
            return self.build(root, root.right, val)
        else:
            return self.build(root, root.left, val)
        return
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self.build(-1, root, val)
        return root