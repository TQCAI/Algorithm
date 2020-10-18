from typing import List
class Solution:

    def dfs(self, i):
        if i >= self.n:
            self.res.append(["".join(row) for row in self.board])
            return
        for j in range(self.n):
            if self.isValid(i, j):
                self.board[i][j] = "Q"
                self.dfs(i + 1)
                self.board[i][j] = "."

    def isValid(self, x, y):
        for i in range(x):
            if self.board[i][y] == "Q":
                return False
        for j in range(y):
            if self.board[x][j] == "Q":
                return False
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        i = x - 1
        j = y + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.board = [['.' for i in range(n)] for j in range(n)]
        self.res = []
        self.dfs(0)
        return self.res

if __name__ == '__main__':
    res = Solution().solveNQueens(11)
    print(res)
