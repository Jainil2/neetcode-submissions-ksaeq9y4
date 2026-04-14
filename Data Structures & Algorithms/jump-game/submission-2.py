class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        count = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= count:
                count = 1
            else:
                count += 1
        return count == 1