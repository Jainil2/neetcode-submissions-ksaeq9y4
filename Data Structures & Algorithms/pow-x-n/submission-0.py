class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = x
        if n > 0:
            for i in range(n - 1):
                res = res * x
        elif n < 0:
            for i in range(-n + 1):
                res = res * (1 / x)
        else:
            return 1.00000
        return res