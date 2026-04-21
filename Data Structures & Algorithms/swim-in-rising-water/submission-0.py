class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]

        q = []
        res = grid[0][0]
        heapq.heappush(q, (grid[0][0], 0, 0))
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True

        def bfs():
            nonlocal res
            while q:
                time, x, y = heapq.heappop(q)
                res = max(res, time)
                if x == m - 1 and y == n - 1:
                    return
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                        heapq.heappush(q, [grid[nx][ny], nx, ny])
                        vis[nx][ny] = True
        bfs()
        return res