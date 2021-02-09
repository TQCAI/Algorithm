#include "bits/stdc++.h"

using namespace std;

// todo: 有空二刷一遍

class Solution {
public:
    vector<vector<int>> nSum(vector<int> &nums, int n, int start, int target) {
        int sz = nums.size();
        vector<vector<int>> ans;
        if (n < 2 || sz < n)
            return ans;
        if (n == 2) {
            int lo = start, hi = sz - 1;
            while (lo < hi) {
                int left = nums[lo];
                int right = nums[hi]; //忘了使用 nums[]
                if (nums[lo] + nums[hi] < target)
                    while (lo < hi && nums[lo] == left) lo++;
                else if (nums[lo] + nums[hi] > target)
                    while (lo < hi && nums[hi] == right) hi--;
                else {
                    ans.push_back({nums[lo], nums[hi]});
                    // 等号判断条件写错
                    while (lo < hi && nums[lo] == left) lo++;
                    while (lo < hi && nums[hi] == right) hi--;
                }
            }
        } else {
            int i = start;
            while (i < sz) { // 与3数和不同，这题的递归函数中考虑了 sz<n 的边界条件， 所以这里的边界条件可以简化
                int cur_num = nums[i];
                vector<vector<int>> cur_ans = nSum(nums, n - 1, i + 1, target - nums[i]);
                if (cur_ans.size() > 0) {
                    for (auto vec:cur_ans) {
                        vec.push_back(nums[i]);
                        ans.push_back(vec);
                    }
                }
                while (i < sz and nums[i] == cur_num) i++;
            }
        }
        return ans;
    }

    vector<vector<int>> fourSum(vector<int> &nums, int target) {
        sort(nums.begin(),nums.end());
        return nSum(nums, 4, 0, target);
    }
};

int main() {
    vector<int> nums = {1, 0, -1, 0, -2, 2};
    vector<vector<int>> ans = Solution().fourSum(nums, 0);
    cout << ans.size();
}