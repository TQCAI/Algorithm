[剑指 Offer 45. 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)

有定理有证明，Python题解用了 `functools.cmp_to_key` ， 自己实现过 `fast_sort`

[剑指 Offer 45. 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)




---

Python题解，重载了 `__lt__` 并将类传给 `key` 参数

[python3简单处理](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/python3jian-dan-chu-li-by-bigkjp97/)

```python
class strSmaller(str):
    def __lt__(self, obj:str):
        return self + obj < obj + self


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        return "".join(sorted(map(str, nums), key=strSmaller))
```

