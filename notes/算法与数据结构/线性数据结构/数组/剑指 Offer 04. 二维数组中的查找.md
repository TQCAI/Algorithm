[剑指 Offer 04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)


- 递归（当成二叉搜索数）

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        N = len(matrix)
        M = len(matrix[0])

        def rec(root: Tuple[int, int]):
            x, y = root
            if not (0 <= x < N and 0 <= y < M):
                return False
            root_val = matrix[x][y]
            if root_val == target:
                return True
            if root_val < target:
                return rec((x + 1, y ))  # 下
            else:
                return rec((x, y - 1))  # 左

        return rec((0, M - 1))
```

- 迭代

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        N = len(matrix)
        M = len(matrix[0])
        x, y = 0, M - 1
        while x < N and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        return False
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210130171724211.png)