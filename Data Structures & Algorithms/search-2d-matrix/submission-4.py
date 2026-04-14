class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        i, c = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        idx = 0
        while i <= c:
            md = i + (c - i) // 2
            if matrix[md][0] <= target and matrix[md][r] >= target:
                idx = md
                break
            elif matrix[md][0] > target:
                c = md - 1
            else:
                i = md + 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[idx][m] == target:
                return True
            elif matrix[idx][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False