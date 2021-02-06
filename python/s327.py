from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        presum = [0] * (N + 1)
        s = 0
        for i in range(1, N + 1):
            s += nums[i - 1]
            presum[i] = s

        def merge_sort(l, r):
            if r - l <= 0:
                return 0
            mid = (l + r) // 2
            res = merge_sort(l, mid) + merge_sort(mid + 1, r)
            a = b = mid + 1
            for i in range(l, mid + 1):
                while a <= r and presum[a] - presum[i] < lower:
                    a += 1  # 此时 a >= lower
                while b <= r and presum[b] - presum[i] <= upper:
                    b += 1  # 此时 b > upper
                res += (b - a)
            # 归并排序
            a, b = l, mid + 1
            merged = []
            while a <= mid and b <= r:
                if presum[a] > presum[b]:
                    merged.append(presum[b])
                    b += 1
                else:
                    merged.append(presum[a])
                    a += 1
            while a <= mid:
                merged.append(presum[a])
                a += 1
            while b <= r:
                merged.append(presum[b])
                b += 1
            for i in range(len(merged)):
                presum[l + i] = merged[i]
            return res

        return merge_sort(0, N)


res=Solution().countRangeSum([-2, 5, -1], -2, 2)
print(res)
