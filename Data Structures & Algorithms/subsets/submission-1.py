class Solution:
    def track(self, i: int, cur: List[int]) -> None:
        if i == self.length:
            self.res.append(cur[:])
            return
        self.track(i + 1, cur)
        cur.append(self.nums[i])
        self.track(i + 1, cur)
        cur.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.length = len(nums)
        self.track(0, [])
        return self.res