n, m = map(int, input().split())
primary, annex = {}, {}
for i in range(1, m + 1):
    x, y, z = map(int, input().split())
    if z == 0:  # 主件
        primary[i] = [x, y]
    else:  # 附件
        if z in annex:  # 第二个附件
            annex[z].append([x, y])
        else:  # 第一个附件
            annex[z] = [[x, y]]
m = len(primary)  # 主件个数转化为物品个数
dp = [[0] * (n + 1) for _ in range(m + 1)]
w, v = [[]], [[]]
for key in primary:
    w_temp, v_temp = [], []
    w_temp.append(primary[key][0])  # 1、主件
    v_temp.append(primary[key][0] * primary[key][1])
    if key in annex:  # 存在主件
        w_temp.append(w_temp[0] + annex[key][0][0])  # 2、主件+附件1
        v_temp.append(v_temp[0] + annex[key][0][0] * annex[key][0][1])
        if len(annex[key]) > 1:  # 存在两主件
            w_temp.append(w_temp[0] + annex[key][1][0])  # 3、主件+附件2
            v_temp.append(v_temp[0] + annex[key][1][0] * annex[key][1][1])
            w_temp.append(w_temp[0] + annex[key][0][0] + annex[key][1][0])  # 3、主件+附件1+附件2
            v_temp.append(v_temp[0] + annex[key][0][0] * annex[key][0][1] + annex[key][1][0] * annex[key][1][1])
    w.append(w_temp)
    v.append(v_temp)
for i in range(1, m + 1):
    for j in range(10, n + 1, 10):  # 物品的价格是10的整数倍
        max_i = dp[i - 1][j]
        for k in range(len(w[i])):
            if j - w[i][k] >= 0:
                max_i = max(max_i, dp[i - 1][j - w[i][k]] + v[i][k])
        dp[i][j] = max_i
print(dp[m][n])
