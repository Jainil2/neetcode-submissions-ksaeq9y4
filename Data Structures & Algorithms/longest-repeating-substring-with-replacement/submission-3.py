class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        arr = [0] * 26
        result = 0
        mx = 0
        while r < len(s):
            idx = ord(s[r]) - ord('A')
            arr[idx] += 1
            mx = max(arr[idx], mx)
            while r - l + 1 - mx > k:
                idx = ord(s[l]) - ord('A')
                arr[idx] -= 1
                l += 1
            result = max(result, r - l + 1)
            r += 1
        return result