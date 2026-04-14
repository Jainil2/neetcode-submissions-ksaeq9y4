class Solution:
    xx = [1, -1, 0, 0]
    yy = [0, 0, -1, 1]
    mx = 2147483647

    def dfs(self, x, y, grid, temp, n, m):
        for k in range(4):
            nx = x + self.xx[k]
            ny = y + self.yy[k]
            if 0 <= nx < n and 0 <= ny < m and temp < grid[nx][ny]:
                grid[nx][ny] = temp
                self.dfs(nx, ny, grid, temp + 1, n, m)

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    self.dfs(i, j, grid, 1, n, m)
