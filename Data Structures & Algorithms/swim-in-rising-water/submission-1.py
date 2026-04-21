class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        
        res = 0
        
        while heap:
            time, x, y = heapq.heappop(heap)
            res = max(res, time)
            
            if x == n-1 and y == n-1:
                return res
            
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))
        
        return res