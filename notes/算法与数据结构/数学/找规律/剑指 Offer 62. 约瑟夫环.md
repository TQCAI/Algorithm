[剑指 Offer 62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)

[换个角度举例解决约瑟夫环](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/huan-ge-jiao-du-ju-li-jie-jue-yue-se-fu-huan-by-as/)

老老实实背公式：

$$f(n, m)=\left\{\begin{array}{ll}0 & n=1 \\ {[f(n-1, m)+m] \% n} & n>1\end{array}\right.$$

```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        pos = 0
        for cur_n in range(1, n + 1):
            pos = (pos + m) % cur_n
        return pos
```

