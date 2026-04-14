# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        q.append(root)
        while q:
            n = len(q)
            temp = []
            for _ in range(n):
                t = q.popleft()
                if t:
                    q.append(t.left)
                    q.append(t.right)
                    temp.append(t.val)
            res.append(temp)
        ans = []
        for tt in res:
            if len(tt) > 0:
                ans.append(tt[-1])
        return ans

        