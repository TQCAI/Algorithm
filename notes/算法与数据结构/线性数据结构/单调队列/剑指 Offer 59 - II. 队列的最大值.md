[剑指 Offer 59 - II. 队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)

```python
class MaxQueue:

    def __init__(self):
        self.queue = collections.deque()
        # monotonous queue
        self.monoq = collections.deque()


    def max_value(self) -> int:
        return self.monoq[0] if self.monoq else -1


    def push_back(self, value: int) -> None:
        # 单调递减队列 (前一个元素大于等于后一个元素)
        while self.monoq and self.monoq[-1] < value:
            self.monoq.pop()
        self.monoq.append(value)
        self.queue.append(value)


    def pop_front(self) -> int:
        if not self.queue:
            return -1
        left = self.queue.popleft()
        if self.monoq[0] == left:
            self.monoq.popleft()
        return left
```
