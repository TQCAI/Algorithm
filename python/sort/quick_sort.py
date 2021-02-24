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


# nums = list(range(10))
# random.shuffle(nums)
nums = [5, 2, 3, 1]


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quick_sort(nums, 0, len(nums))
        return nums

print(Solution().sortArray(nums))