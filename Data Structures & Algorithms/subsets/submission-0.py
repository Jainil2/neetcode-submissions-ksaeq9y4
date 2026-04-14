class Solution:
    def solve(self, ans, nums, n, temp):
        if n == len(nums):
            ans.append(temp[:])
            return
        self.solve(ans, nums, n + 1, temp)
        temp.append(nums[n])
        self.solve(ans, nums, n + 1, temp)
        temp.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.solve(ans, nums, 0, [])
        return ans