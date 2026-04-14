class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cs = "".join(ch for ch in s if ch.isalnum())
        i, j = 0, len(cs) - 1
        while i <= j:
            if cs[i] != cs[j]:
                return False
            i += 1
            j -= 1
        return True