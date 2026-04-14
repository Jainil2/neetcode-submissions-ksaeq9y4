class Solution:
    def sub(self, nums, i, cur):
        if i == len(nums):
            return cur
        cur = cur ^ nums[i]
        first = self.sub(nums, i + 1, cur)
        cur = cur ^ nums[i]
        second = self.sub(nums, i + 1, cur)
        return first + second

    def subsetXORSum(self, nums: List[int]) -> int:
        res = self.sub(nums, 0, 0)
        return res