class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == val:
                j += 1
                continue
            nums[i] = nums[j]
            i += 1
            j += 1
        return i