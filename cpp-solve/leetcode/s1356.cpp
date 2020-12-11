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
    vector<int> sortByBits(vector<int> &arr) {
        vector<int> bits(10001, 0);
        for (int i = 1; i < bits.size(); ++i) {
            bits[i] = bits[i >> 1] + (i & 1);
        }
        // [&bits] 表示闭包中按引用捕获 bits
        sort(arr.begin(), arr.end(), [&bits](int x, int y) -> bool {  //lambda表达式中， -> 可以去掉的
            if (bits[x] < bits[y]) {
                return true;  // 实际上是在重载 < 号
            } else if (bits[x] > bits[y]) {
                return false;
            } else {
                return x < y;  // default
            }
        });
        return arr;
    }
};


int main() {
    vector<int> v{0,1,2,3,4,5,6,7,8};
    Solution().sortByBits(v);
    for(auto e:v){
        bug(e)
    }
    return 0;
}