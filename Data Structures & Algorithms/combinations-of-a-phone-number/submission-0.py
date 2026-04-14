class Solution:
    def track(self, freq, digits, index, temp, output):
        if index == len(digits):
            output.append(temp)
            return
        
        letters = freq[int(digits[index])]
        for ch in letters:
            self.track(freq, digits, index + 1, temp + ch, output)
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        freq = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        output = []
        self.track(freq, digits, 0, '', output)
        return output
