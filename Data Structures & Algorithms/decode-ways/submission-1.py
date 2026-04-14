class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        prev2, prev1 = 1, 1  # dp[0], dp[1]

        for i in range(2, n + 1):
            cur = 0
            one = int(s[i-1:i])
            two = int(s[i-2:i])

            if 1 <= one <= 9:
                cur += prev1
            if 10 <= two <= 26:
                cur += prev2

            prev2, prev1 = prev1, cur  # shift window

        return prev1
