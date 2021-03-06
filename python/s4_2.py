from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            index1 = index2 = 0
            while True:
                # 特殊情况(写错了)
                # if index1 + k > n - 1:
                #     return nums1[n - 1]
                # elif index2 + k > m - 1:
                #     return nums2[m - 1]
                # elif k == 1:
                #     return min(nums1[index1 + k], nums2[index2 + k])
                # ---------------------------
                # nums1 普遍偏小的情况
                if index1 == n:
                    return nums2[index2 + k - 1]
                # nums2 普遍偏小的情况
                if index2 == m:
                    return nums1[index1 + k - 1]
                # 死循环退出条件
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                # 正常情况
                half = k // 2
                new_index1 = min(index1 + half - 1, n - 1)
                new_index2 = min(index2 + half - 1, m - 1)
                if nums1[new_index1] < nums2[new_index2]:
                    k -= new_index1 - index1 + 1
                    index1 = new_index1 + 1  # 忘了 + 1
                else:
                    k -= new_index2 - index2 + 1
                    index2 = new_index2 + 1  # 忘了 + 1

        n = len(nums1)
        m = len(nums2)
        total_len = (n + m)
        if total_len % 2:
            return getKthElement((total_len + 1) // 2)
        else:
            return (getKthElement(total_len // 2) + getKthElement(total_len // 2 + 1)) / 2

Solution().findMedianSortedArrays([1, 3, 4, 9], list(range(9)))
