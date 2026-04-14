class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1
        lm = height[i]
        rm = height[j]
        while i < j:
            if lm < rm:
                i += 1
                lm = max(lm, height[i])
                res += lm - height[i]
            else:
                j -= 1
                rm = max(rm, height[j])
                res += rm - height[j]
        return res