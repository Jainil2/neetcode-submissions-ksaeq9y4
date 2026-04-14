class Solution:
    x = [0, 0, -1, 1]
    y = [-1, 1, 0, 0]
    def dfs(self, board, x, y, n, m):
        if not (0 <= x < n and 0 <= y < m) or board[x][y] != 'O':
            return
        board[x][y] = '#'
        for k in range(4):
            nx = x + self.x[k]
            ny = y + self.y[k]
            self.dfs(board, nx, ny, n, m)

    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        for i in range(n):
            if board[i][m - 1] == 'O':
                self.dfs(board, i, m - 1, n, m)
            if board[i][0] == 'O':
                self.dfs(board, i, 0, n, m)
        for j in range(m):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, n, m)
            if board[n - 1][j] == 'O':
                self.dfs(board, n - 1, j, n, m)
        for i in range(0, n):
            for j in range(0, m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'