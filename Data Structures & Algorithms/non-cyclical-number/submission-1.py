class Solution:
    def isHappy(self, n: int) -> bool:
        happy = [1, 10, 100, 1000]
        seen = set()

        while True:
            sum_ = 0
            while n > 0:
                sum_ += pow(n % 10, 2)
                n = n // 10
            if sum_ in happy:
                return True
            if sum_ in seen:
                return False
            seen.add(sum_)
            n = sum_

