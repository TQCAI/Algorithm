[剑指 Offer 44. 数字序列中某一位的数字](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)

[面试题44. 数字序列中某一位的数字（迭代 + 求整 / 求余，清晰图解）](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/mian-shi-ti-44-shu-zi-xu-lie-zhong-mou-yi-wei-de-6/)

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        # digit: 数字位数， 如 1, 2, 3
        # start： 开始数字，如 1, 10, 100
        # count： 每个位上的计数
        digit = 1
        start = 1
        count = 9
        while n > count:
            n -= count
            # 参数更新
            start *= 10 
            digit += 1
            count = digit * start * 9
        # 确定n对应的是哪个数字
        # 此时的n其实是从0开始的，多了一位数，所以要减去。下同
        num = start + (n - 1) // digit 
        # 确定是num的哪一位
        return int(str(num)[(n - 1) % digit])
```