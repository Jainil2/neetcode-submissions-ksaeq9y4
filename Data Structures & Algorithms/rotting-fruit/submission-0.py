from collections import deque
from typing import List

class Solution:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))  
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0
        while q:
            x, y, t = q.popleft()
            minutes = max(minutes, t)
            for dx, dy in self.dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append((nx, ny, t + 1))

        return minutes if fresh == 0 else -1
