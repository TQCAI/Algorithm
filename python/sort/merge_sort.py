from typing import List


def merge_sort(nums, left, right):
    if right <= left:
        return
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    merged = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            merged.append(nums[i])
            i += 1
        else:
            merged.append(nums[j])
            j += 1
    while i <= mid:
        merged.append(nums[i])
        i += 1
    while j <= right:
        merged.append(nums[j])
        j += 1
    for m in range(len(merged)):
        nums[left + m] = merged[m]


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge_sort(nums, 0, len(nums) - 1)
        return nums


# import random
# nums = list(range(10))
# random.shuffle(nums)
nums = [5, 2, 3, 1]

print(Solution().sortArray(nums))
