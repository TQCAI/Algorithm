[剑指 Offer 51. 数组中的逆序对](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)

```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)

        def merge_sort(l, r):
            if l == r:
                return 0
            mid = (l + r) // 2
            res = merge_sort(l, mid) + merge_sort(mid + 1, r)
            # 统计逆序对数目
            a = l
            for b in range(mid + 1, r + 1):
                while a <= mid and nums[a] <= nums[b]:
                    a += 1
                res += mid - a + 1
            # 做归并排序
            a, b = l, mid + 1
            merged = []
            while a <= mid and b <= r:
                if nums[a] < nums[b]:
                    merged.append(nums[a])
                    a += 1
                else:
                    merged.append(nums[b])
                    b += 1
            while a <= mid:
                merged.append(nums[a])
                a += 1
            while b <= r:
                merged.append(nums[b])
                b += 1
            for i in range(r - l + 1): nums[l + i] = merged[i]
            return res

        return merge_sort(0, N - 1)
```