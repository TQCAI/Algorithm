#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        map<char, int> window;
        map<char, int> need;
        for (char c:p) need[c]++;
        int valid = 0, l = 0;
        vector<int> ans;
        for (int r = 0; r < s.size(); ++r) {
            char c = s[r];
            if (need.count(c)) {
                window[c]++;
                if (window[c] == need[c]) valid++;
            }
            if (r - l + 1 == p.size()) {
                c = s[l];
                if (valid == need.size()) ans.push_back(l);
                if (need.count(c)) {
                    if (window[c] == need[c]) valid--;
                    window[c]--;
                }
                l++;
            }
        }
        return ans;
    }
};

int main() {
    vector<int> ans = Solution().findAnagrams(
            "cbaebabacd",
            "abc"
    );
    cout << ans.size();
}