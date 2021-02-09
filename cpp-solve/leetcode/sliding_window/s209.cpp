#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int> &nums) {
        int sum = 0, l = 0, sz = nums.size() + 1;
        for (int r = 0; r < nums.size(); ++r) {
            sum += nums[r];
            while (sum >= target) {
                int cur_sz = r - l + 1;
                if (cur_sz < sz) sz = cur_sz;
                sum -= nums[l++];
            }
        }
        return sz == nums.size() + 1 ? 0 : sz;
    }
};

int main() {
    vector<int> vec = {2, 3, 1, 2, 4, 3};
    int ans = Solution().minSubArrayLen(
            7,
            vec
    );
    cout << ans;
}