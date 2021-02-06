[剑指 Offer 50. 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)

[面试题50. 第一个只出现一次的字符（哈希表 / 有序哈希表，清晰图解）](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/)

```python
class Solution:
    def firstUniqChar(self, s: str) -> str:
        order_dict = collections.OrderedDict()
        for c in s:
            order_dict[c] = c not in order_dict
        for k, v in order_dict.items():
            if v:
                return k
        return " "
```