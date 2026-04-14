from typing import List

class Solution:
    def track(self, nums: List[int], temp: List[int], ans: List[List[int]], idx: int):
        ans.append(temp[:])  # Always append current subset

        for i in range(idx, len(nums)):
            # Skip duplicates at the same tree level
            if i > idx and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.track(nums, temp, ans, i + 1)
            temp.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()  # Sort to group duplicates
        self.track(nums, [], ans, 0)
        return ans
