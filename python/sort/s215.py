import random
from typing import List


def partition(nums, l, r):
    rix = random.randint(l, r)
    nums[rix], nums[l] = nums[l], nums[rix]

    j = l
    pivot = nums[l]
    for i in range(l + 1, r + 1):
        if nums[i] < pivot:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[l], nums[j] = nums[j], nums[l]
    return j


def partition2(nums, l, r):
    rix = random.randint(l, r)
    nums[rix], nums[l] = nums[l], nums[rix]

    pivot = nums[l]
    while l < r:
        while l < r and nums[r] > pivot:
            r -= 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        while l < r and nums[l] < pivot:
            l += 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
    nums[l] = pivot
    return l


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        target = n - k
        while True:
            index = partition2(nums, l, r)
            if index == target:
                return nums[index]
            elif index < target:
                l = index + 1
            else:
                r = index - 1


lst = [3, 2, 1, 5, 6, 4]
index = Solution().findKthLargest(lst, 2)
print(index)
