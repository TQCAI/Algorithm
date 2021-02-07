[剑指 Offer 61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

[面试题61. 扑克牌中的顺子（集合 Set / 排序，清晰图解）](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/)

```python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        min_, max_ = inf, -inf
        repeat = set()
        for num in nums:
            if num == 0:
                continue
            if num in repeat:
                return False
            repeat.add(num)
            min_ = min(min_, num)
            max_ = max(max_, num)
        if max_ - min_ < 5:
            return True
        return False
```