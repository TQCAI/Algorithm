#include "bits/stdc++.h"
#include "vector_util.h"

using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {

        vector<char> mono_stack;
        for (char c:num) {
            while (!mono_stack.empty() && mono_stack.back() > c && k > 0) {
                mono_stack.pop_back();
                k--;
            }
            mono_stack.push_back(c);
        }
        // 如果 k 没用完
        for (; k > 0; k--) mono_stack.pop_back();
        // 删除前导 0
        string ans = "";
        bool is_leading_zero = true;
        for (auto &digit:mono_stack) {
            if (is_leading_zero && digit == '0') continue;
            is_leading_zero = false;
            ans += digit;
        }
        return ans == "" ? "0" : ans;
    }
};

int main() {
    string ans = Solution().removeKdigits(
            "10", 1
    );
    cout << ans;
}