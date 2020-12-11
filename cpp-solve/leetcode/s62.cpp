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
    int dp[200][200] = {0};

    Solution() {
        dp[0][1] = 1;
        for (int i = 1; i < 101; ++i) {
            for (int j = 1; j < 101; ++j) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
    }

    int uniquePaths(int m, int n) {
        return dp[m][n];
    }
};


int main() {
    Solution s;
    cout << s.uniquePaths(3, 7) << endl;
    cout << s.uniquePaths(1, 100) << endl;
    return 0;
}