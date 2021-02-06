[剑指 Offer 29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

[面试题29. 顺时针打印矩阵（模拟、设定边界，清晰图解）](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/)

做的头痛

```python
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []

        def invalid(l, r, t, b):
            if r < l or b < t:
                return True
            return False

        while True:
            # →→
            for i in range(l, r + 1): res.append(matrix[t][i])
            t += 1
            if invalid(l, r, t, b): break
            # ↓↓
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1
            if invalid(l, r, t, b): break
            # ←←
            for i in range(r, l - 1, -1): res.append(matrix[b][i])
            b -= 1
            if invalid(l, r, t, b): break
            # ↑↑
            for i in range(b, t - 1, -1): res.append(matrix[i][l])
            l += 1
            if invalid(l, r, t, b): break
        return res
```

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
```

```python
def spiralOrder(self, matrix):
    return (matrix and list(matrix.pop(0)) + 
            self.spiralOrder(list(zip(*matrix))[::-1]))
```