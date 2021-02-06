from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        N = len(nums)

        def merge_sort(l, r):
            if l == r:
                return 0
            mid = (l + r) // 2
            res = merge_sort(l, mid) + merge_sort(mid + 1, r)
            # 统计翻转对
            a = l
            for b in range(mid + 1, r + 1):
                while a <= mid and nums[a] <= nums[b] * 2:
                    a += 1  # 此时满足 nums[a] > nums[b]*2 且 a<b
                res += mid - a + 1
            # 归并排序
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
            for i in range(r - l + 1):
                nums[l + i] = merged[i]
            return res

        return merge_sort(0, N - 1)


res = Solution().reversePairs([1, 3, 2, 3, 1])
res = Solution().reversePairs([2, 4, 3, 5, 1])
print(res)
