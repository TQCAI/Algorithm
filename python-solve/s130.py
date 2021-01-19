import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        if not M:
            return
        N = len(board[0])
        if not N:
            return
        visit = [[False] * N for _ in range(M)]
        dxy = list(zip([-1, 1, 0, 0], [0, 0, -1, 1]))
        is_valid = lambda x, y: 0 <= x < M and 0 <= y < N
        for x in range(M):
            for y in range(N):
                if board[x][y] == "O" and not visit[x][y]:
                    queue = collections.deque()
                    queue.append([x, y])
                    visit[x][y] = True
                    touch_bound = False
                    records = [queue[0]]
                    while queue:
                        tx, ty = queue.popleft()
                        for dx, dy in dxy:
                            cx, cy = tx + dx, ty + dy
                            if is_valid(cx, cy):
                                if (not visit[cx][cy]) and board[cx][cy] == "O":
                                    queue.append([cx, cy])
                                    records.append([cx, cy])
                                    visit[cx][cy] = True
                            else:
                                touch_bound = True
                    if not touch_bound:
                        for cx, cy in records:
                            board[cx][cy] = "X"


Solution().solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]])
