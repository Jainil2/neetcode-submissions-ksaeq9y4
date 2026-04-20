class Solution:
    def track(self, nums, i, cur, target, n):
        if i > n:
            return 0
        if i == n and cur == target:
            return 1
        return self.track(nums, i + 1, cur + nums[i - 1], target, n) + self.track(nums, i + 1, cur - nums[i - 1], target, n)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.track(nums, 0, 0, target, n)
        