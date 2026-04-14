class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_t = Counter(t)
        left, right = 0, 0
        formed = 0
        window_counts = {}

        min_len = float('inf')
        min_left = 0
        while right < len(s):

            window_counts[s[right]] = window_counts.get(s[right], 0) + 1
            if s[right] in dict_t and window_counts[s[right]] == dict_t[s[right]]:
                formed += 1

            while left <= right and formed == len(dict_t):

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                window_counts[s[left]] -= 1
                if s[left] in dict_t and window_counts[s[left]] < dict_t[s[left]]:
                    formed -= 1

                left += 1
            right += 1 
        return "" if min_len == float('inf') else s[min_left: min_left + min_len]