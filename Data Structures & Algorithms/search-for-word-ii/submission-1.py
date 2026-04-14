class Node:
    def __init__(self):
        self.child = [None] * 26
        self.flag = False

class Solution:
    def __init__(self):
        self.root = Node()
        self.ans = set()

    def addword(self, word):
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not cur.child[idx]:
                cur.child[idx] = Node()
            cur = cur.child[idx]
        cur.flag = True

    def dfs(self, i, j, board, m, n, cur, path, visited):
        if cur.flag:
            self.ans.add(path)
            cur.flag = False  

        if not (0 <= i < m and 0 <= j < n): 
            return
        if visited[i][j]:
            return

        idx = ord(board[i][j]) - ord('a')
        if not cur.child[idx]:
            return

        visited[i][j] = True
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i + dx, j + dy
            self.dfs(ni, nj, board, m, n, cur.child[idx], path + board[i][j], visited)
        visited[i][j] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        for w in words:
            self.addword(w)

        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, board, m, n, self.root, "", visited)

        return list(self.ans)
