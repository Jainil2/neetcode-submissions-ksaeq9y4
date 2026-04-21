class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        num += 1
        print(num)
        res = []
        while num:
            res.append(num % 10)
            num = num // 10
        res.reverse()
        return res