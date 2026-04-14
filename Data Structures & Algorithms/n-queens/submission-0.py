class Solution:
    def track(self, row, col, diag1, diag2, n, mat, ans):
        if row == n:
            ans.append(["".join(r) for r in mat])
            return

        for j in range(n):
            if j in col or (row - j) in diag1 or (row + j) in diag2:
                continue

            col.add(j)
            diag1.add(row - j)
            diag2.add(row + j)
            mat[row][j] = "Q"

            self.track(row + 1, col, diag1, diag2, n, mat, ans)

            col.remove(j)
            diag1.remove(row - j)
            diag2.remove(row + j)
            mat[row][j] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag1 = set()
        diag2 = set()
        mat = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        self.track(0, col, diag1, diag2, n, mat, ans)
        return ans
