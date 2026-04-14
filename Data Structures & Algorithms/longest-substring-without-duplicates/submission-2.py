class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        start, end = 0, 0
        used_char = {}
        result = 0
        while end < length:
            if s[end] in used_char and used_char[s[end]] >= start:
                start = used_char[s[end]] + 1
            used_char[s[end]] = end
            result = max(result, end - start + 1)
            end += 1
        return result