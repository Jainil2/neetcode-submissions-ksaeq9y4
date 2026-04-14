class Solution:
    def track(self, nums, idx, ans, temp, vis):
        if len(temp) == len(nums):
            ans.append(temp[:])
            return
        for i in range(len(nums)):
            if not vis[i]:
                vis[i] = True
                temp.append(nums[i])
                self.track(nums, i, ans, temp, vis)
                temp.pop()
                vis[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        vis = [False] * (len(nums) + 1)
        self.track(nums, 0, ans, [], vis)
        return ans