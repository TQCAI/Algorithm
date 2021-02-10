#include "bits/stdc++.h"

using namespace std;

// todo: 有空二刷一遍

class Solution {
public:
    int largestRectangleArea(vector<int> &heights) {
        stack<int> left_stack; // right_stack;
        int n = heights.size();
        vector<int> left(n), right(n, n); //fixme: right的初始化要小心，默认值为n
        for (int i = 0; i < heights.size(); ++i) {// 注意是 <=
            while (!left_stack.empty() && heights[i] <= heights[left_stack.top()]) {
                right[left_stack.top()] = i;
                left_stack.pop();
            }
            left[i] = left_stack.empty() ? -1 : left_stack.top();
            left_stack.push(i);
        }
        int ans = -1;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, (right[i] - left[i] - 1) * heights[i]);
        }
        return ans;
    }
};

int main() {
    vector<int> nums = {1, 0, -1, 0, -2, 2};
    vector<vector<int>> ans = Solution().fourSum(nums, 0);
    cout << ans.size();
}