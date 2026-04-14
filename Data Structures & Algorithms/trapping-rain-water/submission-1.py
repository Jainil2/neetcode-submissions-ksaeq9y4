class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        ans = 0
        while l <= r:
            if lmax < rmax:
                lmax = max(height[l], lmax)
                
                ans += lmax - height[l]
                l += 1
            else:
                rmax = max(height[r], rmax)
                
                ans += rmax - height[r]
                r -= 1
        return ans
