class Solution:
    def check(self, piles, m, h) -> int:
        c = 0
        for x in piles:
            if x % m == 0:
                c += x // m 
            else:
                c += x // m + 1 
        print("c: ", c)
        if c > h:
            return False
        else:
            return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        l, r = 0, sum(piles)
        res = float('inf')
        while l <= r:
            m = l + (r - l) // 2
            if m == 0:
                break;
            print("m: ", m)
            t = self.check(piles, m, h)
            if t:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res
        


