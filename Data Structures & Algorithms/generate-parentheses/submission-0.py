class Solution:
    def travel(self, open, close, s, res, n):
        if len(s) == 2 * n:
            res.append(s)
            return 
        if open < n:
            self.travel(open + 1, close, s + '(', res, n)
        if open > close:
            self.travel(open, close + 1, s + ')', res, n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.travel(0, 0, "", res, n)
        return res