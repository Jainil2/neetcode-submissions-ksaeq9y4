class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.backtrack(0, nums, target, [])
        return self.ans

    def backtrack(self, idx: int, nums: List[int], target: int, temp: List[int]):
        if target == 0:
            self.ans.append(temp[:])
            return
        if target < 0:
            return

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break

            temp.append(nums[i])
            self.backtrack(i + 1, nums, target - nums[i], temp)  # Move to next index
            temp.pop()
