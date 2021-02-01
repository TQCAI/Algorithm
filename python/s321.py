from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(lst, k):
            stack = []
            drop = len(lst) - k  # 没想到
            for e in lst:
                # 没想到
                while drop and stack and stack[-1] < e:
                    stack.pop()
                    drop -= 1  # 没想到
                stack.append(e)
            return stack[:k]  # 没想到截断

        def merge(la, lb):
            res = []
            while la or lb:
                # bigger 保证不为空列表
                bigger = la if la > lb else lb
                res.append(bigger[0])
                bigger.pop(0)
            return res

        ret = []
        for sp in range(k + 1):
            if sp <= len(nums1) and k - sp <= len(nums2):
                tmp = merge(
                    pick_max(nums1, sp),
                    pick_max(nums2, k - sp),
                )
                ret = max(ret, tmp)
        return ret


ret = Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
print(ret)
