def quick_sort(nums, a, b):
    if b>=a:
        return
    pivot = nums[a]
    l, r = a, b
    while l < r:
        while l < r and nums[r] > pivot:
            r -= 1
        if l < r:
            nums[l] = nums[r]
            l += 1
        while l < r and nums[l] < pivot:
            l += 1
        if l < r:
            nums[r] = nums[l]
            r -= 1
    nums[l] = pivot
    quick_sort(nums, a, l - 1)
    quick_sort(nums, l + 1, b)


nums = [5, 3, 4, 7]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
