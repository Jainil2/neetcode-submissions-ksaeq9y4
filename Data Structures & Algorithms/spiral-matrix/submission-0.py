class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        left, right, up, down = 0, n - 1, 0, m - 1
        i, x, y = 0, 0, 0
        while left <= right and up <= down and len(res) != m * n:
            if i == 0:
                if y == right:
                    i = 1
                    up += 1
                    continue
                res.append(matrix[x][y])
                x += dir[i][0]
                y += dir[i][1]
            
            elif i == 1:
                if x == down:
                    i = 2
                    right -= 1
                    continue
                res.append(matrix[x][y])
                x += dir[i][0]
                y += dir[i][1]

            elif i == 2:
                if y == left:
                    i = 3
                    down -= 1
                    continue
                res.append(matrix[x][y])
                x += dir[i][0]
                y += dir[i][1]

            elif i == 3:
                if x == up:
                    i = 0
                    left += 1
                    continue
                res.append(matrix[x][y])
                x += dir[i][0]
                y += dir[i][1]
        res.append(matrix[x][y])
        return res