from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lst = []
        for a, b in intervals:
            lst.append([0, a])
            lst.append([1, b])
        a, b = newInterval
        lst.append([0, a])
        lst.append([1, b])
        lst.sort(key=lambda x: (x[1], x[0]))
        pre = -1
        active = False
        processed = []
        for bit, val in lst:
            if pre == 0 and bit == 0:
                active = True
            elif pre == 1 and bit == 1:
                active = False
                processed.append(val)
            elif active:
                pass
            else:
                processed.append(val)
            pre = bit
        res = []
        for i in range(0, len(processed), 2):
            res.append([processed[i], processed[i + 1]])
        return res


# print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
