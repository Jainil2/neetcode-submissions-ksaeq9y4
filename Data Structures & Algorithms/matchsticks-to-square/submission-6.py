class Solution:
    def makesquare(self, m: List[int]) -> bool:
        total = sum(m)
        if total % 4 != 0:
            return False

        side = total // 4
        n = len(m)

        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue

            for i in range(n):
                if mask & (1 << i):
                    continue

                nxt = mask | (1 << i)

                if dp[mask] + m[i] <= side:
                    dp[nxt] = (dp[mask] + m[i]) % side

        return dp[(1 << n) - 1] == 0