#include "bits/stdc++.h"

#define N 1005

using namespace std;

int dp[N][N];  //dp[i][j]表示前i个物品，背包容量是j的情况下的最大价值。
int w[N];
int v[N];

int main() {
    freopen("../data/01bag.txt", "r", stdin);
    int n, m;
    // 物品    容积
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        //          体积  价值
        scanf("%d%d", &v[i], &w[i]);
    // 物品
    for (int i = 1; i <= n; i++) {
        // 重量
        for (int j = 0; j <= m; j++) {
            // 不选
            dp[i][j] = dp[i - 1][j];
            if (j >= v[i])
                // 选                    上个物品
                dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i]] + w[i]);
        }
    }
    cout << dp[n][m] << endl;
    return 0;
}

