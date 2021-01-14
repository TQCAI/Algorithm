nums = [1, 1, 3, 6, 6, 6, 7, 8, 8, 9]


def binary_search(nums, target):
    '''找一个数'''
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        # 如果是Java Cpp
        # mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1


print("binary_search", binary_search(nums, 6))


def lower_bound(nums, target):
    '''找左边界'''
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            r = mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid
    # 对未命中情况进行后处理
    if l == len(nums):
        return -1
    return l if nums[l] == target else -1


print("lower_bound", lower_bound(nums, 6))
print("lower_bound", lower_bound(nums, 2))


def upper_bound(nums, target):
    '''找右边界'''
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid
    if l == 0:
        return -1
    return l - 1 if nums[l - 1] == target else -1


print("upper_bound", upper_bound(nums, 100))
print("upper_bound", upper_bound(nums, -1))
print("upper_bound", upper_bound(nums, 2))
print("upper_bound", upper_bound(nums, 6))
