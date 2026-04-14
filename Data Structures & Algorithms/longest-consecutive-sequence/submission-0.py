class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in num_set:
                start = nums[i] + 1
                c = 1
                while(start in num_set):
                    c += 1
                    start += 1
                res = max(c, res)
        return res