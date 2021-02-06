[剑指 Offer 43. 1～n 整数中 1 出现的次数](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/)

[面试题43. 1～n 整数中 1 出现的次数（清晰图解）](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/mian-shi-ti-43-1n-zheng-shu-zhong-1-chu-xian-de-2/)

TODO: 我的 `low` ,  `high` ,  `digit` 都是用 `str + int` 推出来的，复现题解中的做法 

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        number = str(n)
        L = len(number)
        int_ = lambda x: int(x) if x else 0
        ans = 0
        for i in range(L):
            high = int_(number[:i])
            low = int_(number[i + 1:])
            digit = 10 ** (L - 1 - i)
            if number[i] == '0':
                ans += high * digit
            elif number[i] == '1':
                ans += high * digit + low + 1
            else:
                ans += (high + 1) * digit
        return ans
```