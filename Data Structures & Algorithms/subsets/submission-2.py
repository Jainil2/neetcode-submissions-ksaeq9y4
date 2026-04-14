class Solution:
    def track(self, nums, i, cur, res):
        if i == len(nums):
            res.append(cur[:])
            return
        cur.append(nums[i])
        self.track(nums, i + 1, cur, res)
        cur.pop()
        self.track(nums, i + 1, cur, res)
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.track(nums, 0, [], res)
        return res