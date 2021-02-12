from typing import List


def get_D(weights, w):
    D = 0
    cur_weight = 0
    for weight in weights:
        if cur_weight + weight > w:
            cur_weight = 0
            D += 1
        cur_weight += weight
    return D + 1


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)  # fixme 错在这
        r = sum(weights)
        while l < r:
            mid = (l + r) // 2
            cur_D = get_D(weights, mid)
            if cur_D == D:
                r = mid
            elif cur_D < D:
                # 天数过少，减少最大载重，天数增加
                r = mid
            elif cur_D > D:
                l = mid + 1
        return l


# D = get_D([1, 2, 3, 1, 1], 3)
# print(D)
w = Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(w)
w = Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3)
print(w)
w = Solution().shipWithinDays([1, 2, 3, 1, 1], 4)
print(w)
