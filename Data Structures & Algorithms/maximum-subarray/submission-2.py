class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, cur = nums[0], nums[0]
        for num in nums[1:]:
            res = max(res, cur)
            cur = max(cur + num, num)
        res = max(res, cur)
        return res