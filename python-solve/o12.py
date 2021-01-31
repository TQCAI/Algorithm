from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dt = [-1, 1]
        ct = [0, 0]
        dx, dy = ct + dt, dt + ct
        dd = list(zip(dx, dy))
        N = len(board)
        M = len(board[0])
        is_valid = lambda x, y: 0 <= x < N and 0 <= y < M
        ans = False

        def dfs(pt, n):
            nonlocal ans
            tx, ty = pt
            if word[n] != board[tx][ty]:
                return
            if n >= len(word) - 1:
                ans = True
                return
            for dx, dy in dd:
                cx, cy = tx + dx, ty + dy
                if is_valid(cx, cy) and (not visit[cx][cy]):
                    visit[cx][cy] = 1
                    dfs([cx, cy], n + 1)
                    visit[cx][cy] = 0

        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    visit = [[0] * M for _ in range(N)]
                    visit[i][j] = 1  # 在这里卡住了
                    dfs([i, j], 0)
                    visit[i][j] = 0
                    if ans:
                        return True
        return False


# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"
board = [["a", "a"]]
word = "aaa"
print(Solution().exist(board, word))
