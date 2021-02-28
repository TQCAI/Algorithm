def jump(nums):
    ans = 0
    start = 0
    end = 1
    n = len(nums)
    while end < n:
        max_pos = 0
        for i in range(start, end):
            max_pos = max(max_pos, i + nums[i])
        start = end
        end = max_pos + 1
        ans += 1
    return ans


jump([2, 3, 1, 1, 4])
