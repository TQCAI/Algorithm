[剑指 Offer 49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)

[面试题49. 丑数（动态规划，清晰图解）](https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/)

只会默写代码，不会数学原理

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(n2, n3, n5)
            if n2 == dp[i]: p2 += 1
            if n3 == dp[i]: p3 += 1
            if n5 == dp[i]: p5 += 1
        return dp[-1]
```