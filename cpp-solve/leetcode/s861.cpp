#include <bits/stdc++.h>

#define FF(a, b) for(int a=0;a<b;a++)
#define F(a, b) for(int a=1;a<=b;a++)
#define LEN 200
#define INF ((1<<30)-1)
#define bug(x) cout<<#x<<"="<<x<<endl;

using namespace std;
typedef long long ll;
const double pi = acos(-1);

class Solution {
public:
    int matrixScore(vector<vector<int>> &A) {
        int m = A.size(), n = A[0].size();
        //m 行 n 列
        int ret = m * (1 << (n - 1)); // 忘了 m * ()
        // 先“翻转”行再“翻转”列。翻转行必然使第一列全为1
        for (int j = 1; j < n; ++j) { //遍历第j列
            int nOnes = 0;
            for (int i = 0; i < m; ++i) { //第i行
                if (A[i][0] == 1) {  //如果某一行第一列是0，该行会翻转
                    nOnes += A[i][j]; // 手抖写成  A[i][0]
                } else {
                    nOnes += (1 - A[i][j]);
                }
            }
            int k = max(nOnes, m - nOnes);
            ret += k * (1 << (n - 1 - j));
        }
        return ret;
    }
};

int main() {
    vector<vector<int>> A{{0, 0, 1, 1},
                          {1, 0, 1, 0},
                          {1, 1, 0, 0}};
    int ret = Solution().matrixScore(A);
    bug(ret)
    return 0;
}