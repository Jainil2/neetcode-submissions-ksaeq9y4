class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n - 1
        c = 0
        while i < j:
            c = numbers[i] + numbers[j]
            if c == target:
                return [i + 1, j + 1]
            elif c < target:
                i += 1
            else:
                j -= 1
        return []