[剑指 Offer 39. 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)

一行Python

```python
return collections.Counter(nums).most_common()[0][0]
```

[面试题39. 数组中出现次数超过一半的数字（摩尔投票法，清晰图解）](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/)

- 数组排序法

将数组 `nums` 排序，**数组中点的元素** 一定为众数。

- 摩尔投票法

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        x = 0
        for num in nums:
            if vote == 0:
                x = num
            vote += (1 if num == x else -1)
        return x
```

- 位运算

[排序、Map、分治、Boyer-Moore 摩尔投票、位运算](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/pai-xu-map-fen-zhi-boyer-moore-mo-er-tou-piao-wei-/)

看不懂，感觉鸡肋

