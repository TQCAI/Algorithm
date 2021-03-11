# 数组长度为【n】，切出至少【k】个相同长度为【m】的木块，已知【k】，求【m】
def check(nums, n, mid):
    res = 0
    for i in range(n):
        res += nums[i] // mid
    return res


def cut_wood(nums, k):
    n = len(nums)
    l, r = 1, max(nums)
    while l < r:
        cur_m = (l + r) // 2
        # m越大，k越小
        cur_k = check(nums, n, cur_m)
        if cur_k == k:
            r = cur_m
        elif cur_k < k:
            r = cur_m
        else:
            l = cur_m + 1
    return l


m = cut_wood([4, 7, 2, 10, 5], 5)
print(m)
