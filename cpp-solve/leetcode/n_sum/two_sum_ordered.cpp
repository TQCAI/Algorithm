#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        while (l < r) {
            if (numbers[l] + numbers[r] < target)
                l++;
            else if (numbers[l] + numbers[r] > target)
                r--;
            else
                return {l + 1, r + 1};
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