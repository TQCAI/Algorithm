#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> window;
        // ans 应该初始化为0而不是负数，以适应s为空的情况
        int l = 0, ans = 0;
        for (int r = 0; r < s.size(); ++r) {
            char c = s[r];
            while (window.count(c)) {
                window.erase(s[l++]);
            }
            window.insert(c);
            ans = max(ans, (int) window.size());
        }
        return ans;
    }
};

int main() {
    vector<int> nums = {3, 4, 5, 1, 2};
    int min_num = Solution().minArray(nums);
    cout << min_num;
}