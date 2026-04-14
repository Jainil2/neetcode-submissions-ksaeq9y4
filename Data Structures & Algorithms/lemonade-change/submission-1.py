class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = defaultdict(int)
        for bill in bills:
            freq[bill] += 1
            if bill == 10:
                if freq[5] >= 1:
                    freq[5] -= 1
                else:
                    return False
            elif bill == 20:
                if freq.get(10, 0) >= 1 and freq.get(5, 0) >= 1:
                    freq[10] -= 1
                    freq[5] -= 1
                elif freq.get(5, 0) >= 3:
                    freq[5] -= 3
                else:
                    return False
        return True
