class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = 0
        for x in nums:
            if cur < 0:
                cur = 0
            cur += x
            ans = max(cur, ans)
        return ans