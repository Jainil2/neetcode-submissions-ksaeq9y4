class Solution:
    def track(self, nums, cur, res, used):
        if len(cur) == len(nums):
            if cur not in res:
                res.append(cur[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and (used[i - 1] or used[i]):
                continue
            if used[i]:
                continue
            
            cur.append(nums[i])
            used[i] = True

            self.track(nums, cur, res, used)

            cur.pop()
            used[i] = False

        return

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        self.track(nums, [], res, used)
        return res