[剑指 Offer 57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

[数学问题，数学解决](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shu-xue-wen-ti-shu-xue-jie-jue-by-erik_chen/)

时间复杂度是 $O(\sqrt{target})$

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        # 至少含有两个数
        for n in range(2, target + 1):
            # 分子。 且n*(n-1)必然为偶数，故//2不会有问题
            numerator = target - n * (n - 1) // 2
            # 注意是 <= 0
            if numerator <= 0:
                break
            if numerator % n == 0:
                a = numerator // n
                ans.append(list(range(a, a + n)))
        # 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
        # 当前排列是按照序列大小来排，故从数字大小的角度是降序的，所以要reverse
        return ans[::-1]
```

- 双指针

这个方法虽然容易想到，但是慢多了

[和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/mian-shi-ti-57-ii-he-wei-sde-lian-xu-zheng-shu-x-2/)

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l, r = 1, 2
        ans = []
        while l < r:
            s = (l + r) * (r - l + 1) // 2
            if s == target:
                ans.append(list(range(l, r + 1)))
                l += 1  # 不加爆栈
            elif s < target:
                r += 1
            else:
                l += 1
        return ans
```

- 滑动窗口

其实所谓滑动窗口看起来也是双指针，留给以后思考

[什么是滑动窗口，以及如何用滑动窗口解这道题（C++/Java/Python）](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/)