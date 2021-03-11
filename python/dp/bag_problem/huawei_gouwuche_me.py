from collections import defaultdict

# 总钱数， 物品个数
N, m = map(int, input().split())
N //= 10
primary, appendix = {}, defaultdict(list)
# 遍历物品
for i in range(1, m + 1):
    # 价格 重要度
    price, value, q = map(int, input().split())
    price //= 10
    # 主件
    if q == 0:
        primary[i] = [price, price * value * 10]
    else:
        appendix[q].append([price, price * value * 10])
# 【重要条件】每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。
# 构造分组
n_primary = len(primary)
# 价格向量 与 价值向量
# 轴0：分组id（n_primary个）；轴1：当前分组下的物品id
prices = [[] for _ in range(n_primary + 1)]
values = [[] for _ in range(n_primary + 1)]
for i, prime_id in enumerate(primary, start=1):
    # 主件
    prime_price, prime_value = primary[prime_id]
    prices[i].append(prime_price)
    values[i].append(prime_value)
    # 主件 附件1 |   主件 附件2
    for price, value in appendix[prime_id]:
        prices[i].append(prime_price + price)
        values[i].append(prime_value + value)
    # 主件 附件1  附件2
    if len(appendix[prime_id]) == 2:
        prices[i].append(prime_price + appendix[prime_id][0][0] + appendix[prime_id][1][0])
        values[i].append(prime_value + appendix[prime_id][0][1] + appendix[prime_id][1][1])

dp = [[0] * (N + 1) for _ in range(n_primary + 1)]
for i in range(1, n_primary + 1):
    for j in range(N + 1):
        max_value = dp[i - 1][j]
        for k in range(len(prices[i])):
            price = prices[i][k]
            value = values[i][k]
            if j - price >= 0:
                max_value = max(max_value, dp[i - 1][j - price] + value)
        dp[i][j] = max_value
print(dp[-1][-1])
