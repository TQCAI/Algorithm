from typing import List


def quick_sort(nums, left, right):
    if right <= left:
        return
    i = left
    j = right
    pivot = nums[i]
    while i < j:
        # 找到第一个小于pivot的
        while i < j and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i] = nums[j]
            i += 1
        while i < j and nums[i] < pivot:
            i += 1
        if i < j:
            nums[j] = nums[i]
            j -= 1
        nums[i] = pivot
    quick_sort(nums, left, i - 1)
    quick_sort(nums, i + 1, right)


def partition2(nums, l, r):
    if l >= r:
        return
    pivot = nums[l]
    j = l
    for i in range(l + 1, r+1):
        if nums[i] < pivot:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[l], nums[j] = nums[j], nums[l]
    partition2(nums, l, j - 1)
    partition2(nums, j + 1, r)


# nums = list(range(10))
# random.shuffle(nums)
nums = [5, 2, 3, 1]


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quick_sort(nums, 0, len(nums))
        return nums


# print(Solution().sortArray(nums))

partition2(nums, 0, len(nums)-1)
print(nums)
