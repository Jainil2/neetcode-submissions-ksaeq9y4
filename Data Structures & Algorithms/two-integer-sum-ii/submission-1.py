class Solution:
    def twoSum(self, number: List[int], target: int) -> List[int]:
        l, r = 0, len(number) - 1
        while l < r:
            if number[l] + number[r] == target:
                return [l + 1, r + 1]
            elif number[l] + number[r] > target:
                r -= 1
            if number[l] + number[r] < target:
                l += 1
        return -1