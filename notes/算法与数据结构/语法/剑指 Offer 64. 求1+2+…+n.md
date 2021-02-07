[剑指 Offer 64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)

[面试题64. 求 1 + 2 + … + n（逻辑符短路，清晰图解）](https://leetcode-cn.com/problems/qiu-12n-lcof/solution/mian-shi-ti-64-qiu-1-2-nluo-ji-fu-duan-lu-qing-xi-/)

python的 and 操作如果最后结果为真，返回最后一个表达式的值，or 操作如果结果为真，返回第一个结果为真的表达式的值

```python
class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n-1))
```