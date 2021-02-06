[剑指 Offer 46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

一顿回溯猛如虎，一看题解是DP

- 回溯法

```python
class Solution:
    def translateNum(self, num: int) -> int:
        number2alpha = dict(zip(range(26), [chr(ord('a') + x) for x in range(26)]))
        path = []
        ans = []

        def backtrace(numbers: str):
            if not numbers:
                ans.append("".join(path))
            for i in range(1, len(numbers) + 1):
                cns = numbers[:i]
                cn = int(cns)
                # 这里需要排除 '06' 这样的非法解。
                if not (cns.startswith('0') and len(cns) > 1) and cn <= 25:
                    path.append(number2alpha[cn])
                    backtrace(numbers[i:])
                    path.pop()

        backtrace(str(num))
        return len(set(ans)) # 不去重也可以
```

- 动态规划

[把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-by-leetcode-sol/)

[面试题46. 把数字翻译成字符串（动态规划，清晰图解）](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/)

有空再好好看看，感觉还有很多地方不熟悉

- 无滚动优化

```python
class Solution:
    def translateNum(self, num: int) -> int:
        numbers = str(num)
        L = len(numbers)
        dp = [1] * L
        for i in range(1, L):
            # 注意符合条件后累加的是 dp[i-2], 而不是 1
            dp[i] = dp[i - 1] + (dp[i - 2] if '10' <= numbers[i - 1:i + 1] <= '25' else 0)
        return dp[-1]
```

- 滚动优化

```python
class Solution:
    def translateNum(self, num: int) -> int:
        numbers = str(num)
        L = len(numbers)
        dp0, dp1, dp2 = 1, 1, 1
        for i in range(1, L):
            # 注意符合条件后累加的是 dp[i-2], 而不是 1
            dp2 = dp1 + (dp0 if '10' <= numbers[i - 1:i + 1] <= '25' else 0)
            dp0, dp1 = dp1, dp2
        return dp2
```