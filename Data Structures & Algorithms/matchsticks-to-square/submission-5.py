class Solution:
    def track(self, m, start, cur, s, side, used):
        if s == 3:
            return True
        if cur == side:
            return self.track(m, 0, 0, s + 1, side, used)
        for i in range(start, len(m)):
            if used[i]:
                continue
            if cur + m[i] > side:
                continue
            used[i] = True
            if self.track(m, i + 1, cur + m[i], s, side, used):
                return True
            used[i] = False
        return False
    
    def makesquare(self, m: List[int]) -> bool:
        total = sum(m)
        if total % 4 != 0:
            return False
        m.sort(reverse = True)
        used = [False] * len(m)
        side = total // 4
        return self.track(m, 0, 0, 0, side, used)