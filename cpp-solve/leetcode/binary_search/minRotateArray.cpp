#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    int minArray(vector<int> &nums) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            if (nums[l] < nums[r])
                return nums[l];
            int mid = l + (r - l) / 2;
            if (nums[l] < nums[mid])
                l = mid + 1;
            else if (nums[l] > nums[mid])
                r = mid;
            else
                l++;
        }
        return nums[r];
    }
};

int main() {
    vector<int> nums = {3, 4, 5, 1, 2};
    int min_num=Solution().minArray(nums);
    cout<<min_num;
}