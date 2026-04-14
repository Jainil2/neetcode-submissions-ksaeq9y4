class Solution:
    x = [0, -1, 1, 0]
    y = [1, 0, 0, -1]

    def dfs(self, grid, i, j, n, m):
        grid[i][j] = '0' 
        for k in range(4):
            xx = i + self.x[k]
            yy = j + self.y[k]
            if 0 <= xx < n and 0 <= yy < m and grid[xx][yy] == '1':
                self.dfs(grid, xx, yy, n, m)

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, i, j, n, m)
        return cnt
