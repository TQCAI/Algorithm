#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    vector<vector<int>> twoSum(vector<int> &nums, int lo, int hi, int target) {
        vector<vector<int>> ans;
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
        return ans;
    }

    vector<vector<int>> threeSum(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int i = 0;
        int n = nums.size();
        vector<vector<int>> ans;
        // 试想一下，这是三数之和，假如有 0 1 2，i < (3-2=1)
        while (i < n - 2) {
            int cur_num = nums[i];
            vector<vector<int>> cur_ans = twoSum(nums, i + 1, n - 1, -nums[i]);
            if (cur_ans.size() > 0) {
                for (auto vec:cur_ans) {
                    vec.push_back(nums[i]);
                    ans.push_back(vec);
                }
            }
            while (i < n - 2 and nums[i] == cur_num) i++;
        }
        return ans;
    }
};

int main() {
    vector<int> nums = {1, 2, 3, 4};
    vector<vector<int>> ans = Solution().twoSum(nums, 0, nums.size() - 1, 5);
    vector<int> nums2 = {-1, 0, 1, 2, -1, -4};
    Solution().threeSum(nums2);
    cout << ans.size();
}