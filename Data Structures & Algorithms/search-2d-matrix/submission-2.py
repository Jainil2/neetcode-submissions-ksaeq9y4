class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        i, c = 0, len(matrix) 
        l, r = 0, len(matrix[0]) - 1
        while i < c and matrix[i][0] <= target:
            i += 1
        i -= 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[i][m] == target:
                return True
            elif matrix[i][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False