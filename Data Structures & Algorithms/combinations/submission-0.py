# 1 2 3

class Solution:
    def track(self, n, k, i, cur, res):
        if i > n + 1:
            return
        if len(cur) == k:
            res.append(cur[:])
            return
        cur.append(i)
        self.track(n, k, i + 1, cur, res)
        cur.pop()
        self.track(n, k, i + 1, cur, res)
        return

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.track(n, k, 1, [], res)
        return res