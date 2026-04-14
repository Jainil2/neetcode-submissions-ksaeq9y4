class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for num in nums:
            if num in freq:
                if freq[num] + 1 > n // 2:
                    return num
                freq[num] += 1
            else:
                freq[num] = 1
                if freq[num] + 1 > n // 2:
                    return num
        