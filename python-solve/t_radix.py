def radix_sort(nums):
    """基数排序"""
    i = 0  # 记录当前正在排拿一位，最低位为1
    max_num = max(nums)  # 最大值
    N = len(str(max_num))  # 记录最大值的位数
    while i < N:
        buckets = [[] for _ in range(10)]  # 初始化桶数组
        for num in nums:
            buckets[int(num / (10 ** i)) % 10].append(num)  # 找到位置放入桶数组
        print(buckets)
        nums.clear()
        for bucket in buckets:  # 放回原序列
            for num in bucket:
                nums.append(num)
        i += 1


if __name__ == '__main__':
    a = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
    radix_sort(a)
    print(a)
