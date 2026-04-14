class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            print(m)
            if nums[m] < nums[(m + 1) % len(nums)] and nums[m] < nums[m - 1]:
                return nums[m]
            elif nums[m] < nums[(m + 1) % len(nums)] and nums[m] > nums[m - 1]:
                if nums[m] > nums[-1]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] > nums[-1]:
                    l = m + 1
                else:
                    r = m - 1