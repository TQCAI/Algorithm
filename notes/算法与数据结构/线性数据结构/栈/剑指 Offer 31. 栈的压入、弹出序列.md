[剑指 Offer 31. 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pu_i = 0
        for num in popped:
            if stack and stack[-1] == num:
                stack.pop()
            else:
                while pu_i < len(pushed):
                    cur_push = pushed[pu_i]
                    stack.append(cur_push)
                    pu_i += 1
                    if cur_push == num:
                        break
                if stack[-1] != num:
                    return False
                stack.pop()
        return True
```

[面试题31. 栈的压入、弹出序列（模拟，清晰图解）](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/mian-shi-ti-31-zhan-de-ya-ru-dan-chu-xu-lie-mo-n-2/)

好家伙，看了题解才知道我的思路是反过来的，居然还能AC

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
```