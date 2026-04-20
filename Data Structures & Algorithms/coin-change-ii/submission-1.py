class Solution:
    # def track(self, amount, coins, cur):
    #     if amount < 0:
    #         return 0
    #     if amount == 0:
    #         print(cur[:])
    #         return 1
    #     s = 0
    #     for coin in coins:
    #         cur.append(coin)
    #         s += self.track(amount - coin, coins, cur)
    #         cur.pop()
    #     return s

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        if amount == 0:
            return 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    if coins[i - 1] == j:
                        dp[i][j] = 1 + dp[i][j - coins[i - 1]] + dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(coins)][amount]


        # return self.track(amount, coins, [])


#     0   1   2   3   4 
# 0   0   0   0   0   0
# 1   0   1   1   1   1
# 2   0   1   2   2   3
# 3   0   1   2   3   4
