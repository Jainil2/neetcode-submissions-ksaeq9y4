class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far = max_so_far = result = nums[0]
        for x in nums[1:]:
            choices = (min_so_far * x, max_so_far * x, x)
            max_so_far = max(choices)
            min_so_far = min(choices)
            result = max(result, max_so_far)
        return result