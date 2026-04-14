# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        q.append(root)
        while q:
            temp = []
            n = len(q)
            for _ in range(n):
                t = q.popleft()
                if t:
                    q.append(t.left)
                    q.append(t.right)
                    temp.append(t.val)
            if len(temp) > 0:
                ans.append(temp)
        return ans
