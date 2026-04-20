class Solution:
    def checkValidString(self, s: str) -> bool:
        st1, st2 = [], []
        for i in range(len(s)):
            if s[i] == ')' and not st1 and not st2:
                return False
            elif s[i] == ')' and st1:
                st1.pop()
                continue
            elif s[i] == ')' and st2:
                st2.pop()
                continue
            elif s[i] == '(':
                st1.append(i)
            elif s[i] == '*':
                st2.append(i)
        if len(st1) > len(st2):
            return False
        while st1:
            if st1[-1] > st2[-1]:
                return False
            else:
                st1.pop()
                st2.pop()
        return True