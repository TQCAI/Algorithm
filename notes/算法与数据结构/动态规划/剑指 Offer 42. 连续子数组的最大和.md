[剑指 Offer 42. 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        ans = -inf
        for num in nums:
            sum_ += num
            if sum_ < 0:
                sum_ = 0
                ans = max(ans, num)
            else:
                ans = max(ans, sum_)
        return ans

```