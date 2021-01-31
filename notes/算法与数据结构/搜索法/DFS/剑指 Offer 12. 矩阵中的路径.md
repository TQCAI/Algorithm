[剑指 Offer 12. 矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)

屈辱啊，居然连个DFS都写不出

题解：

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
```

自己复现：

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N, M = len(board), len(board[0])
        L = len(word)
        def dfs(x, y, n) -> bool:
            if not (0<=x<N and 0<=y<M and board[x][y]==word[n]):
                return False
            if n == L - 1:
                return True
            nn=n+1
            board[x][y]=''
            ans = dfs(x-1,y,nn) or  dfs(x+1,y,nn) or  dfs(x,y-1,nn) or  dfs(x,y+1,nn) 
            board[x][y]=word[n]
            return ans
        for x in range(N):
            for y in range(M):
                if dfs(x,y,0):
                    return True
        return False
```
