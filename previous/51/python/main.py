from typing import List


class Solution:

    def dfs(self, i):
        if i >= self.n:
            self.res.append(["".join(row) for row in self.board])
            return
        n = self.n
        for j in range(n):
            dgi = i - j + n
            udgi = i + j
            if self.col[j] != 1 and self.dg[dgi] != 1 and self.udg[udgi] != 1:
                self.board[i][j] = "Q"
                self.col[j] = self.dg[dgi] = self.udg[udgi] = 1
                self.dfs(i + 1)
                self.board[i][j] = "."
                self.col[j] = self.dg[dgi] = self.udg[udgi] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.res = []
        self.col = [0] * n
        self.dg = [0] * (n * 2)
        self.udg = [0] * (n * 2)
        self.dfs(0)
        return self.res


if __name__ == '__main__':
    res = Solution().solveNQueens(4)
    print(res)
