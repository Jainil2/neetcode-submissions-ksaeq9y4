class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            t = prefix - k
            if t in freq:
                count += freq[t]
            freq[prefix] += 1
        return count