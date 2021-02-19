from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        tot = l1 + l2

        def findKthElement(k):
            ix1 = 0
            ix2 = 0
            while True:
                if ix1 == l1:
                    return nums2[ix2 + k - 1]
                if ix2 == l2:
                    return nums1[ix1 + k - 1]
                # 这个判断要放在后面
                if k == 1:
                    return min(nums1[ix1], nums2[ix2])
                nix1 = min(l1 - 1, ix1 + k // 2 - 1)
                nix2 = min(l2 - 1, ix2 + k // 2 - 1)
                if nums1[nix1] < nums2[nix2]:
                    k -= (nix1 - ix1 + 1)
                    ix1 = nix1 + 1
                else:
                    k -= (nix2 - ix2 + 1)
                    ix2 = nix2 + 1

        return findKthElement(tot // 2 + 1) if tot % 2 else (findKthElement(tot // 2) + findKthElement(tot // 2+1)) / 2


ans = Solution().findMedianSortedArrays([2, 3, 4], [5, 6, 7])
print(ans)
