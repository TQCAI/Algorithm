#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        map<char, int> window;
        map<char, int> need;
        for (char c:t) need[c]++;
        int valid = 0, l = 0, a = -1, b = s.size();
        for (int r = 0; r < s.size(); ++r) {
            char c = s[r];
            if (need.count(c)) {
                window[c]++;
                if (window[c] == need[c]) valid++;
            }
            while (valid == need.size()) {
                if (r - l < b - a) {
                    b = r;
                    a = l;
                }
                c = s[l]; // 记得改这里
                if (need.count(c)) {
                    if (window[c] == need[c]) valid--;
                    window[c]--;
                }
                l++;  // 记得更新
            }
        }
        return a == -1 ? "" : s.substr(a, (b - a) + 1);
    }
};

int main() {
    string ans = Solution().minWindow("ADOBECODEBANC",
                                      "ABC"
    );
    cout << ans;
}