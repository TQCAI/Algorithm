# 物品数量，背包容量
N, M = 4, 5
# 从1开始索引，0元素无意义
weight = ["#", 1, 2, 3, 4]
value = ["#", 2, 4, 4, 5]
# 二维数组解决
dp = [[0] * (M + 1) for _ in range(N + 1)]
# 物品方向遍历
for i in range(1, N + 1):
    # 背包容量方向遍历
    for j in range(weight[i], M + 1):
        dp[i][j] = max(
            dp[i - 1][j],  # 不选
            dp[i][j - weight[i]] + value[i],  # 选
        )
ans = dp[-1][-1]
print(ans)

# 压缩为一位数组
dp = [0] * (M + 1)
# 物品方向遍历
for i in range(1, N + 1):
    # 背包容量方向遍历 （从大到小）
    for j in range(weight[i], M + 1):
        dp[j] = max(
            dp[j],  # 选
            dp[j - weight[i]] + value[i],  # 不选
        )
ans = dp[-1]
print(ans)