class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        z = 0
        t = len(nums) - 1
        while i <= t:
            if nums[i] == 0:
                nums[i], nums[z] = nums[z], nums[i]
                i += 1
                z += 1
            elif nums[i] == 2:
                nums[i], nums[t] = nums[t], nums[i]
                t -= 1
            else:
                i += 1
        return nums