[剑指 Offer 56 - I. 数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)

[接地气讲解（分组位运算）「还不懂就来P城砍我」](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)

TODO: 看懂其他解法的题解

```python
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        mix = 0
        for num in nums:
            mix ^= num
        mask = 1
        while (mix & mask) == 0:
            mask <<= 1
        a, b = 0, 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
```