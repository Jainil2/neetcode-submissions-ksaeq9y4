class Solution:
    def check(self, a, b, freq):
        j = 0
        while j < min(len(a), len(b)):
            if freq[b[j]] < freq[a[j]]:
                return False
            elif freq[b[j]] > freq[a[j]]:
                return True
            j += 1
        return len(b) >= len(a)
    def isAlienSorted(self, words: List[str], order: str) -> bool:
            freq = {}
            for i in range(len(order)):
                freq[order[i]] = i
            i, j = 0, 1
            while j < len(words):
                a = words[i]
                b = words[j]
                if not self.check(a, b, freq):
                    return False
                i += 1
                j += 1
            return True