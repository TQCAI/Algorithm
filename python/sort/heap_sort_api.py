from typing import List


import heapq

def heap_sort(nums):
    heapq.heapify(nums)
    res = []
    while nums:
        res.append(heapq.heappop(nums))
    return res


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return heap_sort(nums)


# import random
# nums = list(range(10))
# random.shuffle(nums)
nums = [5, 2, 3, 1]

print(Solution().sortArray(nums))
