class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                c = nums[i] + nums[j] + nums[k] 
                if c == 0:
                    t = [nums[i],nums[j],nums[k]]
                    if t not in res:
                        res.append(t)
                    j += 1
                    k -= 1
                elif c < 0:
                    j += 1
                else:
                    k -= 1
        return res