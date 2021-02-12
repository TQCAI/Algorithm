#include "bits/stdc++.h"
#include "vector_util.h"

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2) {
        vector<int> mono_stack;
        map<int, int> next_bigger;
        int n = nums2.size();
        for (int i = 0; i < n; ++i) {
            while (!mono_stack.empty() && mono_stack.back() < nums2[i]) {
                next_bigger[mono_stack.back()] = nums2[i];
                mono_stack.pop_back();
            }
            mono_stack.push_back(nums2[i]);
        }
        vector<int> ans;
        for (int &num:nums1) {
            int cur = -1;
            if (next_bigger.count(num)) cur = next_bigger[num];
            ans.push_back(cur);
        }
        return ans;
    }
};

int main() {
    vector<int> nums1 = {4, 1, 2}, nums2 = {1, 3, 4, 2};
    vector<int> ans = Solution().nextGreaterElement(
            nums1, nums2
    );
    cout << ans.size();
}