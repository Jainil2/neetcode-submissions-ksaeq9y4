class Solution:
    x = [0, 0, -1, 1]
    y = [-1, 1, 0, 0]
    def bfs(self, heights, vis, x, y, m, n, o):
        q = deque()
        q.append((x, y, o))
        while q:
            temp = q.popleft()
            vis[temp[0]][temp[1]] = 1
            if temp[2] == 'p':
                self.p.add((temp[0], temp[1]))
            else:
                self.a.add((temp[0], temp[1]))
            for k in range(4):
                nx = temp[0] + self.x[k]
                ny = temp[1] + self.y[k]
                if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and heights[nx][ny] >= heights[temp[0]][temp[1]]:
                    q.append((nx, ny, temp[2]))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.p, self.a = set(), set()
        m, n = len(heights), len(heights[0])
        ans = []
        vis1, vis2 = [[0 for _  in range(n)] for _ in range(m)], [[0 for _  in range(n)] for _ in range(m)]
        for i in range(m):
            self.bfs(heights, vis1, i, 0, m, n, 'p')
            self.bfs(heights, vis2, i, n - 1, m, n, 'a')
        for j in range(n):
            self.bfs(heights, vis1, 0, j, m, n, 'p')
            self.bfs(heights, vis2, m - 1, j, m, n, 'a')
        for i in range(m):
            for j in range(n):
                if (i,j) in self.p and (i, j) in self.a:
                    ans.append([i, j])
        return ans
                    
