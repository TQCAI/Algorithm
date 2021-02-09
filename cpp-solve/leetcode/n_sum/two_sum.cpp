#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        map<int, int> sub2ix;
        for (int i = 0; i < nums.size(); ++i) {
            int sub = target - nums[i];
            if (sub2ix.count(sub))
                return {i, sub2ix[sub]};
            else
                sub2ix[nums[i]] = i;
        }
        return {0, 0};
    }
};

int main() {
    vector<int> nums = {2, 7, 11, 15};
    vector<int> ans = Solution().twoSum(nums, 9);
    cout << ans[0] << endl;
    cout << ans[1] << endl;
}