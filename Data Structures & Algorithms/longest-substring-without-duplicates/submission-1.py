class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        l = 0
        vis = {} 

        for r in range(n):
            if s[r] in vis and vis[s[r]] >= l:
                l = vis[s[r]] 
            res = max(res, r - l + 1)
            vis[s[r]] = r + 1 

        return res
