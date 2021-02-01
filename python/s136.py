from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(seq, x):
            l = 0
            r = N = len(seq)
            while l < r:
                mid = (l + r) // 2
                if seq[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            return l if (0 <= l < N and seq[l] == x) else -1

        def upper_bound(seq, x):
            l = 0
            r = N = len(seq)
            while l < r:
                mid = (l + r) // 2
                if seq[mid] > x:
                    r = mid
                else:
                    l = mid + 1
            return l if (0 <= l - 1 < N and seq[l - 1] == x) else -1

        if not nums:
            return -1, -1
        l = lower_bound(nums, target)
        r = upper_bound(nums, target)
        if l == -1:
            return -1, -1
        else:
            return l, r - 1


print(Solution().searchRange([2, 2], 3))
