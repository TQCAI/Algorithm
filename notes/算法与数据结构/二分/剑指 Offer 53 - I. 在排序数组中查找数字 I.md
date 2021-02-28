[剑指 Offer 53 - I. 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

[面试题53 - I. 在排序数组中查找数字 I（二分法，清晰图解）](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/)

看了题解才知道，只用一个upper_bound就可以了

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def lower_bound(nums, x):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == x:
                    r = mid
                elif nums[mid] < x:
                    l = mid + 1
                elif nums[mid] > x:
                    r = mid
            return l

        def upper_bound(nums, x):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == x:
                    l = mid + 1
                elif nums[mid] < x:
                    l = mid + 1
                elif nums[mid] > x:
                    r = mid
            return r

        lb, rb = lower_bound(nums, target), upper_bound(nums, target)
        if lb >= len(nums):
            return 0
        return rb - lb
```

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def upper_bound(nums, x):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == x:
                    l = mid + 1
                elif nums[mid] < x:
                    l = mid + 1
                elif nums[mid] > x:
                    r = mid
            return r

        return upper_bound(nums, target) - upper_bound(nums, target - 1)
```