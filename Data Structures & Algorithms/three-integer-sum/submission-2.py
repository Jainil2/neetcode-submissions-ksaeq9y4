class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        l, n = 0, len(nums) - 1
        while l < n:
            k, r = l + 1, n
            while k < r:
                t = nums[l] + nums[k] + nums[r]
                if t == 0:
                    ans.add((nums[l],nums[k],nums[r]))
                    k += 1
                    r -= 1
                elif t < 0:
                    k += 1
                else:
                    r -= 1
            l += 1
        return list(ans)