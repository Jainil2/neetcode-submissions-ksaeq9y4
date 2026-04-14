class Solution:
    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]

    def dfs(self, grid, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
            return 0
        cnt = 1
        grid[i][j] = 0
        for k in range(4):
            nx = i + self.x[k]
            ny = j + self.y[k]
            cnt +=  self.dfs(grid, nx, ny, n, m)
        return cnt

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = self.dfs(grid, i, j, n, m)
                    ans = max(ans, res)
        return ans