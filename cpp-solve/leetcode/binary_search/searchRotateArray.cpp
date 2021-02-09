#include "bits/stdc++.h"

using namespace std;

// todo: 有空二刷一遍

class Solution {
public:
    int search(vector<int> &nums, int target) {
        int l = 0, r = nums.size() - 1, n = nums.size();
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target)
                return mid;
            // 左边有序
            if (nums[0] <= nums[mid]) {
                // 目标在左边
                if (nums[0] <= target && target < nums[mid])
                    r = mid - 1;
                else
                    l = mid + 1;
            } else { // 右边有序
                // 目标在右边
                if (nums[mid] < target && target <= nums[n - 1])
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }
        return -1;
    }
};

int main() {
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    int res = Solution().search(nums, 0);
    cout << res << endl;
}