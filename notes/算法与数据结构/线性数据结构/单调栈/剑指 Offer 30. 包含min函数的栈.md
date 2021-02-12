[剑指 Offer 30. 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)

[面试题30. 包含 min 函数的栈（辅助栈，清晰图解）](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/solution/mian-shi-ti-30-bao-han-minhan-shu-de-zhan-fu-zhu-z/)

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []


    def push(self, x: int) -> None:
        self.A.append(x)
        # 从栈底往栈顶，是单调递减的
        # 不是 >
        if len(self.B) == 0 or self.B[-1] >= x: 
            self.B.append(x)


    def pop(self) -> None:
        # 其实不用对B是否为空进行判断，因为只要A有元素，B就有
        if self.B and self.B[-1] == self.A.pop():
            self.B.pop()


    def top(self) -> int:
        return self.A[-1]


    def min(self) -> int:
        return self.B[-1]
```