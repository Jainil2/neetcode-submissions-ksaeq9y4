class Solution:
    def track(self, idx, nums, target, cur, temp, n, ans):
        if cur > target or idx >= n:
            return
        if cur == target:
            ans.append(temp[:])
            return
        temp.append(nums[idx])
        self.track(idx, nums, target, cur + nums[idx], temp, n, ans)
        temp.pop()
        self.track(idx + 1, nums, target, cur, temp, n, ans)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        self.track(0, nums, target, 0, [], n, ans)
        return ans