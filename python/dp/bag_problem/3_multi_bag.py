# todo
# 物品数量，背包容量
N, M = 4, 5
# 从1开始索引，0元素无意义
weight = ["#", 1, 2, 3, 4]
value = ["#", 2, 4, 4, 5]
count = ["#", 3, 1, 3, 2]
# 我的一个粗浅的想法：转化为01背包
new_weight = ["#"]
new_value = ["#"]
for i in range(1, N + 1):
    for j in range(count[i]):
        new_weight += [weight[i]] * j
        new_value += [value[i]] * j
weight, value = new_weight, new_value
N = len(weight)
# 二维数组解决
dp = [[0] * (M + 1) for _ in range(N + 1)]
# 物品方向遍历
for i in range(1, N + 1):
    # 背包容量方向遍历
    for j in range(weight[i], M + 1):
        # for k in range(1, count[i] + 1):
        #     pre_weight = j - weight[i] * k
        #     if pre_weight < 0: continue
        dp[i][j] = max(
            dp[i][j],
            dp[i - 1][j],  # 不选
            dp[i - 1][j - weight[i]] + value[i],  # 选
        )
ans = dp[-1][-1]
print(ans)
