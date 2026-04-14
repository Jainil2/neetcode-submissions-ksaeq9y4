class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        freq = {'(': ')', '{': '}', '[':']'}
        for x in s:
            if x in freq:
                st.append(x)
            else:
                if not st or freq[st.pop()] != x:
                    return False
        return len(st) == 0
