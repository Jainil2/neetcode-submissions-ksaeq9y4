class Solution:
    def track(self, i: int, cur: int) -> None:
        if i == self.length:
            self.res += cur
            return
        self.track(i + 1, cur)
        cur = cur ^ self.nums[i]
        self.track(i + 1, cur)
        cur = cur ^ self.nums[i]
        return

    def subsetXORSum(self, nums: List[int]) -> int:
        self.nums = nums
        self.length = len(nums)
        self.res = 0
        self.track(0, 0)
        return self.res