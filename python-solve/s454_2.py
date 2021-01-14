def nSum(nums: list, n: int, start: int, target: int):
    sz = len(nums)
    res = []
    if n < 2 or sz < n:
        return res
    if n == 2:
        lo = start
        hi = sz - 1
        while lo < hi:
            sum = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if sum < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif sum > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
    else:
        i = start
        while i < sz:
            arr_list = nSum(nums, n - 1, i + 1, target - nums[i])
            for arr in arr_list:
                arr.append(nums[i])
                res.append(arr)
            while i < sz - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
    return res


print(nSum([1, 0, -1, 0, -2, 2], 4, 0, 0))

lst=[1,3,4]
