class Solution:
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]
    def track(self, board, i, j, word, idx, vis, m, n):
        if len(word) == idx:
            return True
        for k in range(4):
            new_x = self.x[k] + i
            new_y = self.y[k] + j
            if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == word[idx] and not vis[new_x][new_y]:
                vis[new_x][new_y] = 1
                if self.track(board, new_x, new_y, word, idx + 1, vis, m, n):
                    return True
                vis[new_x][new_y] = 0
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    vis =  [[0 for _ in range(n)] for _ in range(m)]
                    vis[i][j] = 1
                    if self.track(board, i, j, word, 1, vis, m, n):
                        return True
        return False