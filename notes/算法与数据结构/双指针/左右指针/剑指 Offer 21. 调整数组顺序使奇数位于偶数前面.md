[剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)

```python
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            while l<r and nums[l]%2==1:
                l+=1
            while l<r and nums[r]%2==0:
                r-=1
            if l<r:
                nums[l], nums[r] = nums[r], nums[l]
        return nums
```
