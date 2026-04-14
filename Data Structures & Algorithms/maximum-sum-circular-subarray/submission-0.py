class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        max_sum = nums[0]
        cur_max = 0
        min_sum = nums[0]
        cur_min = 0

        for x in nums:
            cur_max = max(cur_max + x, x)
            max_sum = max(max_sum, cur_max)

            cur_min = min(cur_min + x, x)
            min_sum = min(min_sum, cur_min)

            total += x

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)